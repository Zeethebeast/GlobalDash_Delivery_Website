from rest_framework import serializers
from deliveries.models import Delivery, TrackingNumber, DeliveryStatus, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'timestamp']

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = ['status', 'message', 'timestamp']

class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = ['number', 'created_at']

class DeliverySerializer(serializers.ModelSerializer):
    tracking_number = TrackingNumberSerializer(read_only=True)
    statuses = DeliveryStatusSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Delivery
        fields = [
            'id', 'sender', 'receiver', 'departure_location', 'destination_location', 'expected_delivery_date',
            'created_at', 'updated_at', 'tracking_number', 'statuses', 'locations'
        ]
