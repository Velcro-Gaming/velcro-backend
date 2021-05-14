from django.db import models
from django.contrib.auth import get_user_model

from console.models import Console
from game.models import Game

User = get_user_model()


# Create your models here.

class Listing(models.Model):
    STATUS = (
        ("available", "Available"),
        ("swapped", "Swapped"),
        ("rented", "Rented"),
        ("sold", "Sold"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    game = models.ForeignKey(Game, null=True, on_delete=models.PROTECT, related_name="listings")
    console = models.ForeignKey(Console, on_delete=models.PROTECT)

    original_case = models.BooleanField(default=False)

    swap = models.BooleanField(default=False)

    rent = models.BooleanField(default=False)
    rent_amount = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)

    sell = models.BooleanField(default=False)
    sell_amount = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)

    status = models.CharField(max_length=120, choices=STATUS, default="available")
    
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.owner} - {self.game}"

    class Meta:
        unique_together = ("owner", "game", "console")



class SavedListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
        
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user} - {self.game}"