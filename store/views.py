from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime


from .models import *


# Create your views here.

def store(request):
    if request.user.is_authenticated :
        customer =request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        item=[]
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products,'cartItems':cartItems}
    return render(request, 'store/store.html', context)

@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items 
    else:
        items = []
        order = {'get_cart_total' :0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        # total= 0
        total = order.get_cart_total
        cartItems = order.get_cart_items 
        # for item in items :
            
        #    total=total+item.product.price
         # Debug print statements
        
        print("Items")
        
    
    else:
        items = []
        order = {'get_cart_total' :0,'get_cart_items':0,'shipping':False}
        total = 0
        cartItems = order['get_cart_items']

       
    context = {'items': items, 'order': order,'total' : total,'cartItems': cartItems}
    return render(request, 'store/checkout.html',context=context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request) :
     trasaction_id = datetime.datetime.now ().timestamp()
     data = json.loads(request.body)

     if request.user.is_authenticated :
          customer = request.user.customer 
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          total = float(data['form']['total'])
          order.transaction_id = trasaction_id

          if total == order.get_cart_total :
               order.complete = True
          order.save()

          if order.shipping == True :
               ShippingAddress.objects.create(
                    customer=customer,
                    order = order ,
                    address = data ['shipping']['address'],
                    city = data ['shipping']['city'],
                    state= data ['shipping']['state'], 
                    zipcode = data ['shipping']['zipcode'],
                    street = data ['shipping']['street'],
                    landmark = data ['shipping']['landmark'],
               )
     else :
        print('User is not logged in')

     return JsonResponse('Payment Complete',safe=False)