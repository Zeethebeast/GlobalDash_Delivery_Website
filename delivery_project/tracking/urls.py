from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('track/', views.TrackingPageView.as_view(), name='track_page'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
]
