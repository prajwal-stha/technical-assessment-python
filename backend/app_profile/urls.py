from django.urls import path
from backend.app_profile.views import (
    ProfileCreateAPIView,
    ProfileDeleteView,
    ProfileDeleteRecoverView,
    ProfileHardDeleteView)

urlpatterns = [
    path('', ProfileCreateAPIView.as_view()),

    path('delete/<str:pk>/', ProfileDeleteView.as_view(), name="delete_profile"),
    path('recover/<str:pk>/', ProfileDeleteRecoverView.as_view(),
         name="recover_profile"),
    path('permanently-delete/<str:pk>/', ProfileHardDeleteView.as_view(),
         name="hard_delete_profile"),
]
