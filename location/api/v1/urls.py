from django.urls import path, re_path
from location.api.v1 import views as location_views


app_name = 'location'

urlpatterns = [
    #
    path('countries/', location_views.CountryView.as_view()),
    
    #
    path('states/', location_views.StateView.as_view()),
    
    #
    path('cities/', location_views.CityView.as_view()),
]
