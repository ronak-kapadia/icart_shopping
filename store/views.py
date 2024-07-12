from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .models import *

# Create your views here.





def store(request):
    # products = Product.objects.all()
    # context ={'products':products}
    return render(request,'store/store.html')

@login_required
def cart(request):
    return render(request,'store/cart.html')

@login_required
def checkout(request):
    return render(request,'store/checkout.html')
    