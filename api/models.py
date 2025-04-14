from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Model for user management
class KhetsingUser(AbstractUser):
     phone_number = models.CharField(max_length=15, unique=True)
     is_verified = models.BooleanField(default=False)
     rating = models.FloatField(default=0.0)

# Model for Lisitng services
class Listing(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     additional_info_markdown = models.TextField(blank=True, null=True) 
     price = models.FloatField()
     location = models.CharField(max_length=100)
     owner = models.ForeignKey(KhetsingUser, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     listing_type = models.CharField(max_length=10, choices=[('product','Product'),('service','Service')])
     
     # Adding a slug field
     slug = models.SlugField(unique=True, blank=True, null=True)

     # Optional image fields, not compulsory
     image_1 = models.ImageField(upload_to='listing_images/', null=True, blank=True)
     image_2 = models.ImageField(upload_to='listing_images/', null=True, blank=True)
     image_3 = models.ImageField(upload_to='listing_images/', null=True, blank=True)
     image_4 = models.ImageField(upload_to='listing_images/', null=True, blank=True)
     
     def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}")
        super().save(*args, **kwargs)

     def __str__(self):
          return self.title

# Model for Storing and Managing transactions
class Transaction(models.Model):
     buyer = models.ForeignKey(KhetsingUser, on_delete=models.CASCADE, related_name='buyer')
     seller = models.ForeignKey(KhetsingUser, on_delete=models.CASCADE, related_name='seller')
     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
     amount = models.DecimalField(max_digits=10, decimal_places=2)
     created_at = models.DateTimeField(auto_now_add=True)
     is_confirmed_by_buyer = models.BooleanField(default=False)
     is_confirmed_by_seller = models.BooleanField(default=False)
     status = models.CharField(max_length=10, choices=[('pending','Pending'),('completed','Completed'),('cancelled','Cancelled')])

     def release_payment(self):
          if self.is_confirmed_by_buyer and self.is_confirmed_by_seller:
               self.status = 'completed'
               # Mpesa/Econet implementation here
               # remember to take 5% off your payment per successful transaction here
               self.save()

# Model for handling Notifications to users on each end and storing them
class Notification(models.Model):
     user = models.ForeignKey(KhetsingUser, on_delete=models.CASCADE)
     message = models.TextField()
     send_via_whatsapp = models.BooleanField(default=False)
     send_via_email = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
