from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.form_view, name='form-view'),
    path("save/", views.register_form, name='form-register'),
    path("list/", views.get_form, name='form-list'),
    path("modify/<int:item_id>/", views.update_form, name='form-modify'),
    path("delete/<int:item_id>/", views.remove_form, name='form-delete'),
]