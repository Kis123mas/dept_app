from django.urls import path
from . import views
from .views import registerStudent
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('register/student/', registerStudent, name='register_student'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout_user'),
    path('profile/', views.profilePage, name='profile'),
    path('dashboard/', views.dashBoard, name='dashboard'),
    path('contact/', views.contactPage, name='contact'),
    path('about/', views.aboutPage, name='about'),
    path('lecturer/', views.lecturers, name='lecturer'),
    path('nonaca/', views.nonacedemic, name='nonaca'),
    path('technical', views.Technicalpage, name='technical')
]