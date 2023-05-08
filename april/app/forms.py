from django import forms
from django.shortcuts import render,redirect
from .models import Login, Details,SkillsInput,RequirementsInput,status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreation(UserCreationForm):
    GENDER_CHOICES = (
        ('Employer', 'Employer'),
        ('Job-Seeker', 'Job-Seeker'),
    )
    status = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'status'] 


# class CustomUser(User):
#     status = forms.CharField(max_length=20, default='Job-Seeker')

class StatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__" 
        widgets = {
            'password':forms.PasswordInput()
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = "__all__"

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()
    #         # Redirect to your details.html page
    #         return redirect('details.html')
    #     return user

    # class Meta:
    #     model = Details
    #     fields = '__all__'

class SkillsInputForm(forms.ModelForm):
    class Meta:
        model = SkillsInput
        fields = "__all__"

class RequirementsInputForm(forms.ModelForm):
    class Meta:
        model = RequirementsInput
        fields = "__all__"