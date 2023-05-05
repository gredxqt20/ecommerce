from django.urls import path
from . import views
from .controller import cart, checkout

urlpatterns = [
    path('home', views.home, name="home"),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name="checkout"),
    path('place-order',checkout.placeorder,name="placeorder")
]
