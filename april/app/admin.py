from django.contrib import admin
from .models import Login,Details,employer_dashboard,jobseeker_dashboard,job_applicants, status, RequirementsInput
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(status)
admin.site.register(Login)
admin.site.register(Details)
admin.site.register(employer_dashboard)
admin.site.register(jobseeker_dashboard)
admin.site.register(job_applicants)
admin.site.register(RequirementsInput)
