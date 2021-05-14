from django.contrib import admin
from order.models import Order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'listing', '_type', 'fee', 'duration', 'is_active', 'created_at' ]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)