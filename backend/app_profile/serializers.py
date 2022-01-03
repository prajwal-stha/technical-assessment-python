from rest_framework import serializers
from backend.app_profile.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
