from django.contrib import admin
from .models import KhetsingUser, Listing, Transaction, Notification

# Register your models here.
admin.site.register(KhetsingUser)
admin.site.register(Listing)