from django.urls import path, re_path
from order.api.v1 import views as order_views


app_name = 'order'

urlpatterns = [
    #
    path('all/', order_views.OrderListView.as_view()),
    
    #
    path('<int:id>/', order_views.OrderDetailView.as_view()),
    
    #
    path('', order_views.OrderCreateView.as_view()),
]
