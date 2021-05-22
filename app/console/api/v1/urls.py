from django.urls import path, re_path
from console.api.v1 import views as console_views


app_name = 'console'

urlpatterns = [
        
    # User Console Detail View
    path('user/<int:user>/<int:id>/', console_views.UserConsoleDetailView.as_view()),

    # User Console List View
    path('user/<int:user>/all/', console_views.UserConsoleListView.as_view()),

    # User Console Register View
    path('user/', console_views.UserConsoleRegisterView.as_view()),



    # Console Detail View
    path('<int:id>/', console_views.ConsoleDetailView.as_view()),

    # Console List View
    path('all/', console_views.ConsoleListView.as_view()),
]
