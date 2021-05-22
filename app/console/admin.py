from django.contrib import admin
from console.models import Console, UserConsole


# Register your models here.

class UserConsoleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'console', ]

    class Meta:
        model = UserConsole


admin.site.register(UserConsole, UserConsoleAdmin)


class ConsoleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'short_name', 'is_active', ]
    list_editable = ['is_active', 'short_name']

    class Meta:
        model = Console


admin.site.register(Console, ConsoleAdmin)