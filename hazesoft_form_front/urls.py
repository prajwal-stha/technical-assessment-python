from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.form_create_view, name='form-creator'),
]