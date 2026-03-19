from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('track/', views.TrackingPageView.as_view(), name='track_page'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
    path('live-tracking/', TemplateView.as_view(template_name='live_tracking.html'), name='live_tracking'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('careers/', TemplateView.as_view(template_name='careers.html'), name='careers'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('api-docs/', TemplateView.as_view(template_name='api_docs.html'), name='api_docs'),
]
