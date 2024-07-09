from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.





def store(request):
    return render(request,'store/store.html')

@login_required
def cart(request):
    return render(request,'store/cart.html')

@login_required
def checkout(request):
    return render(request,'store/checkout.html')
    