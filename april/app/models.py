from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password



# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class status(models.Model):
    status = models.CharField(max_length=20, choices=(('employer','Employer'),('jobseeker','Jobseeker')))


class Details(models.Model):
    F_name= models.CharField(max_length=255, null=True, blank=True)
    S_name= models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255,null=True, blank=True)
    email_address= models.EmailField(max_length=255,null=True, blank=True)
    years_of_experience= models.CharField(max_length=200,null=True, blank=True)
    education_history=models.CharField(max_length=1000,null=True, blank=True)
    acquired_skills=models.CharField(max_length=200,null=True, blank=True)
    other_skills=models.CharField(max_length=200,null=True, blank=True)





class employer_dashboard(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    post_job_opening = models.CharField(max_length=3000)
    view_job_applicants= models.CharField(max_length=255)

class jobseeker_dashboard(models.Model):
    username =models.CharField(max_length=255,primary_key=True)
    upload_resume = models.CharField(max_length=3000)
    upload_skills= models.CharField(max_length=3000)
    view_qualified_jobs = models.CharField(max_length=3000)

class job_applicants(models.Model):
     username = models.CharField(max_length=255,primary_key=True)
     view_resumes_sent = models.CharField(max_length=100000)
     rank_resumes_sent =  models.CharField(max_length=100000)

class SkillsInput(models.Model):
    skills = models.TextField()

class RequirementsInput(models.Model):
    
    job_name= models.CharField(max_length=100,null=True, blank=True)
    years_of_experience= models.CharField(max_length=200,null=True, blank=True)
    skills=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.job_name
    


