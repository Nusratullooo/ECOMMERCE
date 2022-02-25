from django.urls import path

from order import views

urlpatterns = [
    path('shopcart/', views.shopcart, name='shopcart'),
    path('addtoshopcart/<int:pk>/', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('deleteallfromcart/', views.deleteallfromcart, name='deleteallfromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]
