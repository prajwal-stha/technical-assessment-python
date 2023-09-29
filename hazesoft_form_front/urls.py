from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.form_view, name='form-view'),
    path("save/", views.register_form, name='form-register'),
    path("list/", views.get_form, name='form-list'),
]