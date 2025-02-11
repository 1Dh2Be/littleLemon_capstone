from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView),
    path('menu/<int:pk>', views.SingleMenuItemView),
    path('booking/tables', views.BookingViewSet, name='booking_list'),
    path('booking/tables/<int:pk>', views.booking_detail, name='booking_detail'),
]