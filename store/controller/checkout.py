import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from store.models import Cart, Order, OrderItem, Product


# @login_required(login_url='loginpage')
def index(request):
    # rawcart = Cart.objects.filter(user=request.user)
    rawcart = Cart.objects.filter(user=1)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=1)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    context = {'cartitems': cartitems, 'totalprice': total_price}
    return render(request, "store/products/checkout.html", context)


# @login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.county = request.POST.get('county')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode = request.Post.get('payment_mode')
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        neworder.totalprice = cart_total_price
        trackno = 'ecom' + str(random.randint(111111, 999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'ecom' + str(random.randint(111111, 999999))
        neworder.tracking_no = trackno

        neworder.save()
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )
            # To decrease the product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # To clear user's Cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "Your order has been placed successfully")
    return redirect('/')
