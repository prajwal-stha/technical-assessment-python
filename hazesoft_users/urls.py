from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_form_view, name='user-login'),
    path("logout/", views.logout_view, name='user-logout'),
]