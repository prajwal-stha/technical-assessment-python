from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.views.generic.base import View
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from backend.app_profile.models import Profile
from backend.app_profile.serializers import ProfileModelSerializer


class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer


class ProfileDeleteView(View):
    """
    View to handle profile move to trash.
    """
    model = Profile
    permission_classes = [IsAdminUser, ]

    def get(self, request, pk, **kwargs):
        profile = get_object_or_404(Profile, id=pk)
        profile.handle_delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class ProfileDeleteRecoverView(View):
    """
    View to handle profile move to trash.
    """
    model = Profile
    permission_classes = [IsAdminUser, ]

    def get(self, request, pk, **kwargs):
        profile = get_object_or_404(Profile, id=pk)
        profile.handle_delete(recover=True)
        return redirect(self.request.META.get('HTTP_REFERER'))


class ProfileHardDeleteView(DeleteView):
    """
    View to handle profile permanent delete.
    """
    model = Profile
    permission_classes = [IsAdminUser]

    def get_success_url(self) -> str:
        return self.request.META.get('HTTP_REFERER')

    def dispatch(self, request, *args, **kwargs):
        """ A dispatcher to avoid confirmation template """
        if request.user.is_superuser:
            handler = getattr(self, 'delete')
            return handler(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
