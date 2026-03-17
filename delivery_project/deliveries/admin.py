from django.contrib import admin
from .models import Delivery, TrackingNumber, DeliveryStatus, Location

class TrackingNumberInline(admin.StackedInline):
    model = TrackingNumber

class DeliveryStatusInline(admin.TabularInline):
    model = DeliveryStatus
    extra = 1

class LocationInline(admin.TabularInline):
    model = Location
    extra = 1

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'departure_location', 'destination_location', 'expected_delivery_date', 'get_tracking_number', 'current_status')
    inlines = [DeliveryStatusInline, LocationInline]
    readonly_fields = ('get_tracking_number',)

    def get_tracking_number(self, obj):
        return obj.tracking_number.number if hasattr(obj, 'tracking_number') else '-'
    get_tracking_number.short_description = 'Tracking Number'

    def current_status(self, obj):
        latest = obj.statuses.first()
        return latest.get_status_display() if latest else '-'
    current_status.short_description = 'Current Status'

@admin.register(TrackingNumber)
class TrackingNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'delivery', 'created_at')
    search_fields = ('number',)

@admin.register(DeliveryStatus)
class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'latitude', 'longitude', 'timestamp')
