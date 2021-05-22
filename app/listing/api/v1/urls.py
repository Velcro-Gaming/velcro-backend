from django.urls import path, re_path
from listing.api.v1 import views as listing_views


app_name = 'listing'

urlpatterns = [

    # Listing List View
    path('games/', listing_views.ListedGamesView.as_view()),

    # Listing List View
    path('all/', listing_views.ListingListView.as_view()),
    
    # Listing Detail View
    path('<int:id>/', listing_views.ListingDetailView.as_view()),

    # Listing List and Create View
    path('', listing_views.ListingCreateView.as_view()),
]
