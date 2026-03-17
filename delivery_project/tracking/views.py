from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from deliveries.models import Delivery

class HomeView(TemplateView):
    template_name = 'home.html'

class TrackingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'tracking/track.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if tracking_number was passed as GET parameter
        tracking_number = self.request.GET.get('tracking_number', '')
        context['tracking_number'] = tracking_number
        return context

class UserDashboardView(LoginRequiredMixin, ListView):
    model = Delivery
    template_name = 'tracking/dashboard.html'
    context_object_name = 'deliveries'

    def get_queryset(self):
        # Only return deliveries for the logged-in user
        return Delivery.objects.filter(customer=self.request.user).order_by('-created_at')
