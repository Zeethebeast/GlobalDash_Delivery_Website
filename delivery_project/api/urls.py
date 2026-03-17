from django.urls import path
from .views import TrackDeliveryView

urlpatterns = [
    path('track/<str:tracking_number>/', TrackDeliveryView.as_view(), name='api-track-delivery'),
]
