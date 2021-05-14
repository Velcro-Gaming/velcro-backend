from django.contrib import admin
from location.models import Country, State, City

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'full_name', 'country_code', 'calling_code', 'region_code', 'sub_region_code', 'capital',
        'citizenship', 'currency', 'currency_code', 'currency_symbol', 'currency_decimals', 'iso2', 'iso3', 'flag'
    ]
    search_fields = ('name', 'full_name', 'country_code')
    # raw_id_fields = ["category"]

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'country']
    search_fields = ('name', 'country__name', 'country__full_name')
    raw_id_fields = ["country"]

    class Meta:
        model = State


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'state']
    search_fields = ('name', 'state__name', 'state__country__name', 'state__country__full_name')
    raw_id_fields = ["state"]

    class Meta:
        model = City


admin.site.register(City, CityAdmin)



