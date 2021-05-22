from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)

    country_code = models.CharField(max_length=5, blank=True, null=True)
    calling_code = models.CharField(max_length=5, blank=True, null=True)

    region_code = models.CharField(max_length=5, blank=True, null=True)
    sub_region_code = models.CharField(max_length=5, blank=True, null=True)

    capital = models.CharField(max_length=50, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)

    currency = models.CharField(max_length=50, blank=True, null=True)
    currency_code = models.CharField(max_length=50, blank=True, null=True)
    currency_symbol = models.CharField(max_length=50, blank=True, null=True)
    currency_decimals = models.CharField(max_length=5, blank=True, null=True)

    iso2 = models.CharField(max_length=5, blank=True, null=True)
    iso3 = models.CharField(max_length=5, blank=True, null=True)

    flag = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=120)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    capital = models.BooleanField(default=False)

    class Meta:
        ordering = ['country', 'name']

    def __str__(self):
        return f"{self.name} | {self.country}"

    def is_capital(self):
        return self.capital


class City(models.Model):
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['state', 'name']

    def __str__(self):
        return f"{self.name} | {self.state}"


