from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from django.conf.urls.static import static

from accounts.api.v1.views import auth as auth_views

app_name = 'v1'

urlpatterns = [

    # Orders
    path('order/', include('order.api.v1.urls', namespace='order')),

    # Listings
    path('listing/', include('listing.api.v1.urls', namespace='listing')),

    # Games
    path('game/', include('game.api.v1.urls', namespace='game')),

    # Consoles
    path('console/', include('console.api.v1.urls', namespace='console')),

    # Accounts
    path('account/', include('accounts.api.v1.urls', namespace='account')),

    # Locations
    path('location/', include('location.api.v1.urls', namespace='location')),

    # Authentication
    path('login/', auth_views.LoginView.as_view()),  # Login
    path('register/', auth_views.UserCreateView.as_view()),  # Register

]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
