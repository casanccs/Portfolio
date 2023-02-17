from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('createProfile/', createProfile, name='createProfile'),
    path('editProfile/', editProfile, name='editProfile'),
    path('wishlist/', wishlist, name='wishlist'),
    path('createProduct/', createProduct, name='createProduct'),
    path('myListings/', myListings, name='myListings'),
    path('editProduct/<int:product_id>', editProduct, name='editProduct'),
    path('productView/<int:product_id>', productView, name='productView'),
    path('cart/', cart, name='cart'),
    path('deleteItem/<int:item_id>', deleteItem, name='deleteItem'),
    path('editItem/<int:item_id>', editItem, name='editItem'),
    path('purchase/', purchase, name='purchase'),
    path('yourOrders/', yourOrders, name='yourOrders'),
    path('ongoingOrders/', ongoingOrders, name='ongoingOrders'),
    path('shipping/<int:order_id>', shipping, name='shipping'),
    path('aDeliveries/', aDeliveries, name='aDeliveries'),
    path('delivery/<int:order_id>', deliver, name='deliver'),
    path('myDeliveries/', myDeliveries, name='myDeliveries'),
    path('delivered/<int:order_id>', delivered, name='delivered'),
    path('help/', help, name='help'),
    path('tolist/<int:product_id>', tolist, name='tolist'),
    path('deleteReview/<int:review_id>', deleteReview, name='deleteReview'),
]


