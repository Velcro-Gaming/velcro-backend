from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from engine.utils import random_string_generator

from listing.models import Listing

User = get_user_model()


# Create your models here.

class Order(models.Model):
    ORDER_TYPES = (
        ("buy", "Buy"),
        ("rent", "Rent"),
        ("swap", "Swap")
    )

    reference = models.CharField(max_length=120, blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    _type = models.CharField(max_length=120, choices=ORDER_TYPES)

    fee = models.DecimalField(max_digits=7, decimal_places=2)
    duration = models.DurationField(blank=True, null=True)
    offered_listings = models.ManyToManyField(Listing, related_name="orders")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.reference


def order_pre_save_receiver(instance, *args, **kwargs):
    if not instance.reference:
        instance.reference = "vc" + random_string_generator(size=8)
        

pre_save.connect(order_pre_save_receiver, sender=Order)



