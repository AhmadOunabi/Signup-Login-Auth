from django.contrib import admin
from django.urls import path
from registration.views import register,user_login

urlpatterns = [
    path('', register, name='register'),
    path('', user_login, name='user_login'),
]
