from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from deliveries.models import Delivery, TrackingNumber
from .serializers import DeliverySerializer

class TrackDeliveryView(generics.RetrieveAPIView):
    serializer_class = DeliverySerializer
    
    def get_object(self):
        tracking_number = self.kwargs.get('tracking_number')
        try:
            tracking = TrackingNumber.objects.select_related('delivery').get(number=tracking_number)
            return tracking.delivery
        except TrackingNumber.DoesNotExist:
            raise NotFound(detail="Delivery with this tracking number not found.")
