from django.contrib import admin
from django.urls import path
from registration.views import register,user_login,charts_view,charts_plotly

urlpatterns = [
    path('', register, name='register'),
    path('', user_login, name='user_login'),
    path('', charts_view, name='charts_view'),
    path('', charts_plotly, name='charts_view'),
]
