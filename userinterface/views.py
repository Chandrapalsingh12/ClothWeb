from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest

from mainapp import settings
from.models import Product, Orders, OrderUpdates
from math import ceil

import json

from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import razorpay

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 

# Create your views here.
def home(request):
    allProds = []
    catProd = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProd}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslide), nslide])
        
    product_list = {'allProds': allProds}

    return render(request,"index.html",product_list)

@csrf_exempt
def UserSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform = request.POST['conform']

        usercheck = User.objects.filter(username=username)
        emailcheck = User.objects.filter(email=email)

        if emailcheck:
            messages.error(request,"Email Already Taken")
            return redirect('/')

        if usercheck:
            messages.error(request,"Username Alredy Taken")
            return redirect("/")

        if password != conform:
            messages.error(request,"Password Doesn't match")
            return redirect("/")

        else:
            newUser = User.objects.create_user(username, email, password)
            newUser.conform = conform
            newUser.save()
            messages.success(request, "Account Created Successfully")
            return redirect("/")
    return render(request,"base.html")

@csrf_exempt
def UserLoginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        usercheck = User.objects.filter(username=username)
        passcheck = User.objects.filter(password=password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Succssfully Login")
            return redirect(home)
        else:
            messages.error(request,"Please Input Correct username or Password!")
            return redirect(home)

    
    return render(request,"base.html")


def UserLogout(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect(home)



def ProductView(request, myid):
    product = Product.objects.filter(id=myid)

    return render(request,'productview.html',{"product": product[0]})

def searchMatch(query, item):
    if query in item.desc or query in item.product_name or query in item.category:
        return True
    else:
        return False
       
        
def Productsearch(request):
    query = request.GET.get('search')
    allProds = []
    catProd = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProd}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) !=0:
            allProds.append([prod, range(1, nslide), nslide])
    product_list = {'allProds': allProds}

    return render(request,"search.html",product_list)

@csrf_exempt
def ProductCheckout(request):
    if request.method == "POST":
        json_des = request.POST['itemjson']
        price = request.POST['amount']
        name = request.POST['name']
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        pincode = request.POST['pincode']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['pnumber']

        orederProduct = Orders(json_des=json_des, name=name, email=email, address1=address1, address2=address2, city=city, pincode=pincode,state=state,phone=phone,price=price)
        orederProduct.save()

        thanks=True
        update = OrderUpdates(order_id = orederProduct.order_id, update_desc="The Order has been placed")
        update.save()
        id = orederProduct.order_id
        # return render(request,"checkout.html",{'thanks':thanks,'id':id})
        currency = 'INR'
        amount = price
    # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'http://127.0.0.1:8000/cheackout/paymenthandler/'
    
        # we need to pass these details to frontend.
        context= {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url        
        context['ids'] = id        
    
        return render(request,"razerpay.html",context=context)

    return render(request,"checkout.html")
@csrf_exempt
def ProductTracker(request):
    if request.method == "POST":
        orderid = request.POST['orderId']
        emails = request.POST['email']
        # return HttpResponse(f"{orderid} and {emails}")
        try:
            order = Orders.objects.filter(order_id=orderid, email=emails)
            if len(order)>0:
                update = OrderUpdates.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        
        except Exception as e:
            return HttpResponse('{}')
                    
    return render(request,"track.html")
    
def DetailCheck(request):

    detailscheck = Orders.objects.all()
    contex = {'details':detailscheck}
    
    return render(request,"detailcheck.html", contex)

@csrf_exempt
def paymenthandler(request):   
 
    # only accept POST request.
    if request.method == "POST":
        
      
        return render(request, 'paymentsuccess.html')        
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()