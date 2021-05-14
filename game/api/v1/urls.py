from django.urls import path, re_path
from game.api.v1 import views as game_views


app_name = 'game'

urlpatterns = [
    # Game List View
    path('all/', game_views.GameListView.as_view()),
    
    # Game Detail View: Id
    path('<int:id>/', game_views.GameSearchView.as_view()),

    # Game Detail View: Slug
    path('<slug:slug>/', game_views.GameSearchView.as_view()),

    # Game List and Create View
    path('', game_views.GameRegisterView.as_view()),
]
