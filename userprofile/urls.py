# -*- coding:utf-8 -*-
from . import views
from django.urls import path
app_name = "userprofile"

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name="logout")
]