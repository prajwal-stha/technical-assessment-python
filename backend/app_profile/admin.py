from django.contrib import admin
from backend.app_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "gender"]
