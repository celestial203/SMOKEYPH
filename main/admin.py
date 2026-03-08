"""
Django admin configuration for main app.
"""
from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "time", "location", "guests", "status", "created_at"]
    list_filter = ["status", "location", "date"]
    search_fields = ["name", "email", "phone"]
    readonly_fields = ["created_at"]
    list_editable = ["status"]
