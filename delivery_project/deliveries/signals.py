from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
from .models import Delivery, TrackingNumber, DeliveryStatus, DeliveryStatusChoices

@receiver(post_save, sender=Delivery)
def delivery_post_save(sender, instance, created, **kwargs):
    if created:
        def create_initial_tracking():
            # Generate a Tracking Number automatically
            tracking_num = TrackingNumber.generate_number()
            TrackingNumber.objects.create(delivery=instance, number=tracking_num)
            
            # Create an initial PENDING status Only if none exist (admin might have created one inline)
            if not instance.statuses.exists():
                DeliveryStatus.objects.create(delivery=instance, status=DeliveryStatusChoices.PENDING, message="Delivery order created.")
            
            # Send Email Notification
            if instance.customer_email:
                send_mail(
                    subject=f'Delivery Created: {tracking_num}',
                    message=f'Dear Customer,\n\nYour delivery has been created.\nTracking Number: {tracking_num}\nFrom: {instance.sender}\nTo: {instance.receiver}\n\nYou will be notified of further updates.',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
                    recipient_list=[instance.customer_email],
                    fail_silently=True,
                )
        
        transaction.on_commit(create_initial_tracking)

@receiver(post_save, sender=DeliveryStatus)
def delivery_status_post_save(sender, instance, created, **kwargs):
    if created:
        def send_status_email():
            delivery = instance.delivery
            # Only send email if it's not the initial PENDING status created alongside the Delivery
            if delivery.statuses.count() > 1 and delivery.customer_email:
                tracking_num = delivery.tracking_number.number if hasattr(delivery, 'tracking_number') else 'Unknown'
                status_display = instance.get_status_display()
                send_mail(
                    subject=f'Delivery Update: {tracking_num} - {status_display}',
                    message=f'Dear Customer,\n\nYour delivery status has been updated to: {status_display}.\nMessage: {instance.message or "No additional message."}\n\nTrack your delivery on our website using your tracking number: {tracking_num}.',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
                    recipient_list=[delivery.customer_email],
                    fail_silently=True,
                )
        
        transaction.on_commit(send_status_email)
