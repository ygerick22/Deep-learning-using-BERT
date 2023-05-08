from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base, name='home'),
    path('status/', views.Status, name='status'),
    path('login/',views.Login, name='login'),
    path('logout/',views.Logout, name='logout'),
    path('employer/', views.employer, name='employer'),
    path('seeker/', views.seeker, name='seeker'), 
    path('signup/', views.signup1, name='signup'),
    path('account/', views.accounts, name='account'),
    path('details/', views.details, name= 'details'),
    path('SkillsInput/',views.SkillsInput, name= 'SkillsInput'),
    path('RequirementsInput',views.RequirementsUser, name= 'RequirementUser'),
    path('upload_resume/', views.Resume, name='uploads'),
    path('job_opening/', views.opening, name='job-open'),
    path('job_applicants/', views.applicants, name='job-applicant')
    # path('nlp/', views.nlp_view, name='nlp_view')
]


