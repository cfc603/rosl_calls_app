from django.contrib import admin

from .models import IncomingCall, PhoneNumber


@admin.register(IncomingCall)
class IncomingCallAdmin(admin.ModelAdmin):

    list_display = ("__str__", "created")
    readonly_fields = ("created",)


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass
