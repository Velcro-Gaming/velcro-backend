from django.contrib import admin
from listing.models import Listing


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'game', 'rent', 'swap', 'sell', 'is_active' ]

    class Meta:
        model = Listing


admin.site.register(Listing, ListingAdmin)