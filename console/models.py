from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

from engine.utils import unique_slug_generator

User = get_user_model()


# Create your models here.

class Console(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)

    short_name = models.CharField(max_length=120)
    
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


def console_pre_save_receiver(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        

pre_save.connect(console_pre_save_receiver, sender=Console)



class UserConsole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consoles")
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
        
    is_active = models.BooleanField(default=True)

    added_on = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()

    class Meta:
        unique_together = ("user", "console")

    def __str__(self):
        return f"{self.user} - {self.console}"