from django.urls import path, re_path
from accounts.api.v1.views import account as account_views

from .passwords import views as password_views

app_name = 'accounts'

urlpatterns = [
    
    # User Details [RUD]
    path('<int:id>/', account_views.UserDetailView.as_view(), name='detail'),

    # User Details [RUD]
    path('all/', account_views.UserListView.as_view(), name='list'),

    # User Extra Registration
    path('<int:id>/registration/extra/', account_views.UserExtraRegistrationView.as_view(), name='create'),

    # Password Change
    path('password/change/', password_views.PasswordChangeView.as_view(),
         name='password-change'),
]
