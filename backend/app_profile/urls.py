from django.urls import path
from backend.app_profile.views import ProfileCreateAPIView

urlpatterns = [
    path('', ProfileCreateAPIView.as_view())
]
