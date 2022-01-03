from rest_framework.generics import CreateAPIView
from backend.app_profile.models import Profile
from backend.app_profile.serializers import ProfileModelSerializer


class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer
