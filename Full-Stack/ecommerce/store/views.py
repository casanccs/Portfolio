from .models import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from datetime import date


#This will be the main redirect
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    profile = Profile.objects.get(user__exact=request.user)
    if profile.type == "Vendor":
        return HttpResponseRedirect(reverse('myListings'))
    if profile.type == "Transit":
        return HttpResponseRedirect(reverse('aDeliveries'))
    if request.method == "POST":
        products = Product.objects.filter(title__icontains=request.POST['search']).filter(unlisted__exact=False)
    else:
        products = Product.objects.filter(unlisted__exact=False)
    context = {
        'placeholder': "Search for Products",
        'profile': profile,
        'products': products,
    }
    return render(request, 'store/index.html', context)

def help(request):
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'placeholder': 'Does Not Use Search',
        'profile': profile,
    }
    return render(request, 'store/help.html', context)


#Everyone
def loginView(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return HttpResponseRedirect(reverse('login'))
        else:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request,'store/login.html', {})


#Everyone
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

#Everyone
def createProfile(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName']
        )
        profile = Profile(user=user, address=request.POST['address'], phone=request.POST['phone'], picture=request.FILES['picture'], type=request.POST['type'])
        photoFile = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(photoFile.name, photoFile)
        user.save()
        profile.save()
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'store/createProfile.html', {})

#Everyone
def editProfile(request):
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'profile': profile,
    }
    if request.method == 'POST':
        form = request.POST
        profile.user.username = form['username']
        profile.user.email = form['email']
        profile.user.first_name = form['firstName']
        profile.user.last_name = form['lastName']
        profile.address = form['address']
        profile.phone = form['phone']
        profile.type = form['type']
        print(request.FILES)
        if request.FILES:
            profile.picture = request.FILES['picture']
            fs = FileSystemStorage()
            photoFile = request.FILES['picture']
            fs.save(photoFile.name, photoFile)
        profile.user.save()
        profile.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'store/editProfile.html', context)

#Only customers
def wishlist(request):
    profile = Profile.objects.get(user__exact=request.user)
    wishlist = profile.wishlist

    context = {
        'profile': profile,
        'wishlist': wishlist,
    }

    return render(request, 'store/wishlist.html', context)


#Only vendors
#Does not need to search
def createProduct(request):
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'placeholder': 'Does Not Use Search',
        'profile': profile,
    }
    if request.method == "POST":
        form = request.POST
        product = Product(seller=profile, title=form['title'], desc=form['desc'], 
                          price=float(form['dollar'])+0.01*float(form['cents']), picture=request.FILES['picture'])
        fs = FileSystemStorage()
        photoFile = request.FILES['picture']
        fs.save(photoFile.name, photoFile)
        product.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'store/createProduct.html', context)


#Only vendors
def myListings(request):
    profile = Profile.objects.get(user__exact=request.user)
    #implement ordering
    products = Product.objects.filter(seller__exact=profile).order_by('title')
    if request.method == 'POST':
        try:
            products = Product.objects.filter(seller__exact=profile).order_by(request.POST['filter'])
        except:
            if request.POST['search'] == "":
                products = Product.objects.filter(seller__exact=profile).order_by('title')
            else:
                products = Product.objects.filter(seller__exact=profile).filter(title__icontains=request.POST['search'])
    
    productPhotos = productPhoto.objects.filter(product__seller__exact=profile) #This may change, but I get all of the product photo's whose product belongs to the profile
    productReview = productPhoto.objects.filter(product__seller__exact=profile)
    context = {
        'profile': profile,
        'products': products,
        'productPhotos': productPhotos,
        'productReview': productReview,
        'placeholder': 'Search through your offered Products',
    }

    return render(request, 'store/myListings.html', context)

#Validation needs to be checked for the cents entry
#No search
def editProduct(request, product_id):
    profile = Profile.objects.get(user__exact=request.user)
    product = Product.objects.get(id__exact=product_id)
    context = {
        'placeholder': 'Does Not Use Search',
        'profile': profile,
        'product': product,
        'dollar': int(product.price),
        'cents': str(product.price)[-2:],
    }
    if request.method == "POST":
        form = request.POST
        product.title=form['title']
        product.desc=form['desc']
        product.price=float(form['dollar'])+0.01*float(form['cents'])
        if request.FILES:
            product.picture=request.FILES['picture']
            fs = FileSystemStorage()
            photoFile = request.FILES['picture']
            fs.save(photoFile.name, photoFile)
        product.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'store/editProduct.html', context)

#No search
def productView(request, product_id):
    profile = Profile.objects.get(user__exact=request.user)
    product = Product.objects.get(id__exact=product_id)
    if request.method == "POST":
        try:
            quantity = int(request.POST['quantity'])
            addcart = productInCart(profile=profile, product=product, quantity=quantity, totalCost=float(product.price)*quantity)
            addcart.save()
            return HttpResponseRedirect(reverse('cart'))
        except:
            review = productReview(profile=profile, product=product, 
                                   desc=request.POST['desc'], score=int(request.POST['score']))
            review.save()
            product.averageScore = (product.averageScore*product.nReviews + review.score)/(product.nReviews + 1)
            product.nReviews += 1
            product.save()
            return HttpResponseRedirect(reverse('productView', kwargs={'product_id': product_id}))
    reviews = productReview.objects.filter(product__exact=product)
    nReviews = reviews.count()
    totalScore = 0
    for review in reviews:
        totalScore += review.score
    toReview = True
    if productReview.objects.filter(profile__exact=profile).count() > 0:
        toReview = False
    context = {
        'profile': profile,
        'product': product,
        'placeholder': 'Does Not Use Search',
        'reviews': reviews,
        'nReviews': nReviews,
        'totalScore': totalScore,
        'toReview': toReview,
    }


    return render(request, 'store/productView.html', context)

#Search cart
def cart(request):

    profile = Profile.objects.get(user__exact=request.user)
    incart = productInCart.objects.filter(profile__exact=profile)
    if request.method == 'POST':
        incart = incart.filter(product__title__icontains=request.POST['search'])
    totalCost = 0
    for item in incart:
        totalCost += item.totalCost
    context = {
        'profile': profile,
        'incart': incart,
        'total': totalCost,
        'placeholder': 'Find Product in your Cart',
    }
    return render(request, 'store/cart.html', context)

def deleteItem(request, item_id):
    item = productInCart.objects.get(id__exact=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('cart'))

#No search
def editItem(request, item_id):
    profile = Profile.objects.get(user__exact=request.user)
    item = productInCart.objects.get(id__exact=item_id)
    product = Product.objects.get(id__exact=item.product.id)
    context = {
        'profile': profile,
        'product': product,
        'placeholder': 'Does Not Use Search',
    }
    if request.method == "POST":
        quantity = int(request.POST['quantity'])
        addcart = productInCart(profile=profile, product=product, quantity=quantity, totalCost=float(product.price)*quantity)
        addcart.save()
        item.delete()
        return HttpResponseRedirect(reverse('cart'))


    return render(request, 'store/productView.html', context)


def purchase(request):
    profile = Profile.objects.get(user__exact=request.user)
    incart = productInCart.objects.filter(profile__exact=profile)
    for item in incart:
        order = Order(buyer=profile, product=item.product, status="Waiting for order confirmation", quantity=item.quantity, totalCost=float(item.product.price)*item.quantity)
        order.save()
        item.delete()

    context = {
        'profile': profile,
    }

    return HttpResponseRedirect(reverse('yourOrders'))

#Search for orders
def yourOrders(request):
    profile = Profile.objects.get(user__exact=request.user)
    if request.method == "POST":
        orders = Order.objects.filter(buyer__exact=profile).filter(product__title__icontains=request.POST['search'])
    else:
        orders = Order.objects.filter(buyer__exact=profile)

    context = {
        'profile': profile,
        'orders': orders,
        'placeholder': 'Search through your Orders',
    }

    return render(request, 'store/yourOrders.html', context)

#Search
#Need to make "Delivered" to be last, and "Waiting for..." to be first
def ongoingOrders(request):
    profile = Profile.objects.get(user__exact=request.user)
    orders = Order.objects.filter(product__seller__exact=profile)

    if request.method == "POST":
        orders = orders.filter(product__title__icontains=request.POST['search'])
    context = {
        'profile': profile,
        'orders': orders,
        'placeholder': 'Search through your Ordered Products',
    }

    return render(request, 'store/ongoingOrders.html', context)


def shipping(request, order_id):
    order = Order.objects.get(id__exact=order_id)
    order.status = "Shipping"
    order.save()
    return HttpResponseRedirect(reverse('ongoingOrders'))

#Search
def aDeliveries(request):
    profile = Profile.objects.get(user__exact=request.user)
    orders = Order.objects.filter(status__exact="Shipping")
    if request.method == "POST":
        orders = orders.filter(product__title__icontains=request.POST['search'])
    context = {
        'profile': profile,
        'orders': orders,
        'placeholder': 'Search for Available Deliveries',
    }

    return render(request, 'store/aDeliveries.html', context)

def deliver(request, order_id):
    profile = Profile.objects.get(user__exact=request.user)
    order = Order.objects.get(id__exact=order_id)
    order.status = "On Delivery"
    order.deliverer = profile
    order.save()
    return HttpResponseRedirect(reverse('aDeliveries'))

#Search
def myDeliveries(request):
    profile = Profile.objects.get(user__exact=request.user)
    orders = Order.objects.filter(deliverer__exact=profile)
    if request.method == "POST":
        orders = orders.filter(product__title__icontains=request.POST['search'])
    context = {
        'profile': profile,
        'orders': orders,
        'placeholder': 'Search for the Deliveries you have accepted',
    }

    return render(request, 'store/myDeliveries.html', context)

def delivered(request, order_id):
    profile = Profile.objects.get(user__exact=request.user)
    order = Order.objects.get(id__exact=order_id)
    order.status = "Delivered"
    order.date_delivered = date.today()
    order.save()
    return HttpResponseRedirect(reverse('myDeliveries'))

def tolist(request, product_id):
    product = Product.objects.get(id__exact=product_id)
    product.unlisted = not product.unlisted
    product.save()
    return HttpResponseRedirect(reverse('myListings'))

#Must validate/limit access here
def deleteReview(request, review_id):
    review = productReview.objects.get(id__exact=review_id)
    product = review.product
    product.nReviews -= 1
    if product.nReviews == 0:
        product.averageScore = 0
    else:
        product.averageScore = (product.averageScore*(product.nReviews+1) - review.score)/product.nReviews
    review.delete()
    product.save()

    return HttpResponseRedirect(reverse('productView', kwargs={'product_id': product.id}))