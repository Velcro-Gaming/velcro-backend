from django.db import models
from django.db.models.signals import pre_save

from console.models import Console
from engine.utils import unique_slug_generator

# Create your models here.

class Game(models.Model):
    CATEGORY_LIST = (
        ("action", "Action"),
        ("adventure", "Adventure"),
        ("racing", "Racing"),
        ("sport", "Sport"),
        ("strategy", "Strategy"),
        ("others", "Others")
    )

    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)

    category = models.CharField(max_length=120, choices=CATEGORY_LIST)

    consoles = models.ManyToManyField(Console)

    image = models.ImageField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)

    added_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


def game_pre_save_receiver(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        

pre_save.connect(game_pre_save_receiver, sender=Game)


