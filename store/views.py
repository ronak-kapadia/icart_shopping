# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import *

# # Create your views here.

# def store(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'store/store.html', context)

# @login_required
# def cart(request):
#     if request.user.is_authenticated :
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False) 
#         items = order.orderitem_set.all()  

#         #debbuging
#         print(f"Customer: {customer}")
#         print(f"Order: {order}")
#         print(f"Items: {items}")
        
#     else :
#         items = []
   
#     context = {'items':items}
#     return render(request,'store/cart.html')
# @login_required
# def checkout(request):
#     return render(request,'store/checkout.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total' :0,'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        # total= 0
        total = order.get_cart_total
        # for item in items :
            
        #    total=total+item.product.price
            
        
        
         # Debug print statements
        
        print(f"Items: {items}")
        
    
    else:
        items = []
        order = {'get_cart_total' :0,'get_cart_items':0}
        total = 0

       
    context = {'items': items, 'order': order,'total' : total}
    return render(request, 'store/checkout.html',context=context)
