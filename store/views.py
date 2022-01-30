from django.shortcuts import render

# Create your views here.
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request , 'index.html' , context)