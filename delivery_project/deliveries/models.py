from django.db import models
from django.conf import settings
import uuid

class Delivery(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    customer_email = models.EmailField(blank=True, null=True, help_text="Email to send notifications to")
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    departure_location = models.CharField(max_length=255, null=True, blank=True, help_text="Starting point of the delivery")
    destination_location = models.CharField(max_length=255, null=True, blank=True, help_text="Final destination of the delivery")
    expected_delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery from {self.sender} to {self.receiver}"

class TrackingNumber(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, related_name='tracking_number')
    number = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

    @classmethod
    def generate_number(cls):
        return str(uuid.uuid4()).replace('-', '').upper()[:12]

class DeliveryStatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_TRANSIT = 'IN_TRANSIT', 'In Transit'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'

class DeliveryStatus(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=20, choices=DeliveryStatusChoices.choices, default=DeliveryStatusChoices.PENDING)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.delivery} - {self.get_status_display()}"

class Location(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='locations')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.delivery} @ {self.latitude}, {self.longitude}"
