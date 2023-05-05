from django.shortcuts import render, redirect
from pyexpat.errors import messages

from store.models import Category, Product


def home(request):
    return render(request, "store/index.html")

def my_view(request):
    data = Product.objects.values('name')
    return render(request, 'store/inc/navbar.html', {'data': data})


def collections(request):
    category = Category.objects.filter
    context = {'category': category}
    return render(request, "store/collections.html", context)


def collectionsview(request, slug):
    if Category.objects.filter(slug=slug):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "no such category found")
        return redirect('collections')
