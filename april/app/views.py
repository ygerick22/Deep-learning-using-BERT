from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm
from .forms import DetailsForm, UserCreation, StatusForm, RequirementsInputForm
from .models import Details, Login, RequirementsInput
from django.contrib.auth.decorators import login_required
from django.views import View
import torch
import os
import sys
from django.db import models
import torch.nn as nn
import torch.optim as optim
import transformers
from transformers import BertModel, BertTokenizer, AdamW, get_linear_schedule_with_warmup
from app.resume_classifier import ResumeClassifier
from django.contrib import messages

# Add the base directory of your Django project to the system path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Import the ResumeClassifier class from the resume.py file
# from app.models import ResumeClassifier


import sys
print(sys.path)

# Create your views here.
@login_required(login_url='login')
def Status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        if status == 'employer':
                # redirect to employer page
             return redirect ('employer')
        else:
                # redirect to job seeker page
            return redirect ('seeker')
        
    status = StatusForm()
    context = {
        'status':status
    }
    return render (request, 'status.html', context)

def Base(request):
    return render (request, 'base.html')


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('status')

    else:
        form = LoginForm()   

    return render(request, 'login.html', {'form':form})

def Logout(request):
    logout(request)
    return render(request, 'logout.html')

def signup1(request):
    if request.method == 'POST':
        user =UserCreation(request.POST)
        if user.is_valid():
            user = user.save()
            # custom_user = CustomUser.objects.create(user=user, status=user.cleaned_data['status'])
            # custom_user.save()
            return redirect('login')
    else:
        user = UserCreation()
        # Customize error messages
        user.fields['username'].error_messages = {'required': 'Please enter a valid username.',
                                                'unique': 'This username is already taken.'}
        user.fields['password1'].error_messages = {'required': 'Please enter a valid password.'}
        user.fields['password2'].error_messages = {'required': 'Please confirm your password.',
                                                'mismatch': 'The passwords do not match.'}
    context = {'user':user}
    return render(request, 'signup1.html', context)

@login_required(login_url='login')
def accounts(request):
    if request.method == 'POST':
        account = DetailsForm(request.user)
        if account.is_valid:
            phone = request.POST.get('phone_number')
            email = request.POST.get('email_adddres')
            acc = account(phone_number=phone, email_address=email)
            acc.save()
    account = DetailsForm()
    return render(request, 'account.html', {'account' : account})


@login_required(login_url='login')
def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details.html')
    else:
        form = DetailsForm()
    return render(request, 'details.html', {'form':form})



@login_required(login_url='login')
def employer(request):
    return render(request,'employer_dashboard.html')


@login_required(login_url='login')
def seeker(request):
    return render(request,'jobseeker_dashboard.html')

@login_required(login_url='login')
def opening(request):
    details = RequirementsInput.objects.all()
    context = {'details':details}
    return render(request, 'JobOpenings.html', context)

@login_required(login_url='login')
def applicants(request):
    details = Details.objects.all()
    context = {'details':details}
    return render(request, 'applicant.html', context)


@login_required(login_url='login')
def SkillsInput(request):
    return render(request,'SkillsInput.html')


@login_required(login_url='login')
def RequirementsUser(request):
    if request.method == 'POST':
        form= RequirementsInputForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= RequirementsInputForm()
    context = {'form':form}
    return render(request,'EmployerPost.html',context)


import datasets 
import optuna 
from datasets import load_dataset 
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from os import path
import numpy as np
from numpy import argmax
# path = '/kaggle/working/'


# Load the model
loaded_model = AutoModelForSequenceClassification.from_pretrained(
    "resume_yg",
    num_labels=25
)

# Load the tokenizer
loaded_tokenizer = AutoTokenizer.from_pretrained(
    "resume_yg",
)

# Max length
MAX_LENGTH = 512

def Resume(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # Get the user's input from the form
            # job_name = form.cleaned_data['job_name']

            education_history = form.cleaned_data['education_history']
            acquired_skills = form.cleaned_data['acquired_skills']
            other_skills = form.cleaned_data['other_skills']
            
            
            details = education_history + ' ' + acquired_skills + ' ' + other_skills 
            print(details)

            class_dict = {0: 'Advocate',
                        1: 'Arts',
                        2: 'Automation Testing',
                        3: 'Blockchain',
                        4: 'Business Analyst',
                        5: 'Civil Engineer',
                        6: 'Data Science',
                        7: 'Database',
                        8: 'DevOps Engineer',
                        9: 'DotNet Developer',
                        10: 'ETL Developer',
                        11: 'Electrical Engineering',
                        12: 'HR',
                        13: 'Hadoop',
                        14: 'Health and fitness',
                        15: 'Java Developer',
                        16: 'Mechanical Engineer',
                        17: 'Network Security Engineer',
                        18: 'Operations Manager',
                        19: 'PMO',
                        20: 'Python Developer',
                        21: 'SAP Developer',
                        22: 'Sales',
                        23: 'Testing',
                        24: 'Web Designing'}

            def get_result(text, class_dict, message=True):
                encoded_input = loaded_tokenizer(text, truncation=True, padding='max_length',
                                                max_length=MAX_LENGTH, return_tensors='pt')
                output = loaded_model(**encoded_input)
                result = output[0].detach().numpy()
                probs = torch.sigmoid(output[0]).detach().numpy()
                class_label = np.argmax(result)
                label_name = class_dict[class_label]
    
                if message:
                    result = f'The predicted career is label: {label_name} with a probability of {probs[0][class_label]}'
                
                return result, label_name  

            # Return the predicted class as a JSON response
                # return JsonResponse({'predicted_class': result})
            # Run your result through the function
            result, label_name = get_result(details, class_dict)

            # Save the user input to the database
            form.save()

            # Render the template with the predicted category and saved user input
            return render(request, 'prediction.html', {'form': form, 'category':label_name})
    else:
        form = DetailsForm()
    return render(request, 'uploadResume.html', {'form': form})








