from django.contrib import admin
from backend.app_profile.models import Profile, ProfileTrash
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "gender", "delete_action"]

    def get_queryset(self, *args):
        return super().get_queryset(*args).filter(deleted=False)

    def delete_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:maroon;" href="{}">Delete</a>',
            reverse('delete_profile', args=[obj.pk])
        )
    delete_action.short_description = 'Delete'
    delete_action.allow_tags = True


@admin.register(ProfileTrash)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "gender",
                    "recover_action", "hard_delete_action"]

    def get_queryset(self, *args):
        return super().get_queryset(*args).filter(deleted=True)

    def recover_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:green;" href="{}">Recover</a>',
            reverse('recover_profile', args=[obj.pk])
        )
    recover_action.short_description = 'Recover'
    recover_action.allow_tags = True

    def hard_delete_action(self, obj):
        return format_html(
            '<a class="button" style="background-color:maroon;" href="{}">Delete</a>',
            reverse('hard_delete_profile', args=[obj.pk])
        )
    hard_delete_action.short_description = 'Delete'
    hard_delete_action.allow_tags = True

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request) -> bool:
        return False
