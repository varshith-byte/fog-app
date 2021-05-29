from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('fileupload', views.fileupload, name='fileupload'),
    path('table', views.table, name='table'),
    path('user_registration', views.user_registration, name='user_registration'),
    path('logout', views.logout_user, name='logout'),
    path('user_login', views.user_login, name='user_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('savefile', views.save_file, name='savefile'),

]
