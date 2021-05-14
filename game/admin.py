from django.contrib import admin
from game.models import Game


# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'category', ]

    class Meta:
        model = Game


admin.site.register(Game, GameAdmin)