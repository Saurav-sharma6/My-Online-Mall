from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.

def index(request):
    # Fetching all products from database
    #products = Product.objects.all()
    '''
        Now we want list of lists of all different categories. For that we do the following :-
        Step 1.  Get categories of all objects present in database. Dublicate values are also present.
        Step 2.  Apply set comprehension to find unique values of all posible categories.
        STEP 3.  For each item of set (getting from step2) we get all items having same category by
                    applying filter. After that we make list of common category products, range and
                    number of slides required to display common items assuming 4 products in one slide.
    '''
    allprods = []
    catprods = Product.objects.values('category','id')   # STEP 1
    cats = {item['category'] for item in catprods}   # STEP 2
    # STEP 3
    for cat in cats:
        products = Product.objects.filter(category = cat)
        # Calculating number of slides required
        n = len(products)
        nSlides = (n//4) + ceil((n/4)-(n//4))
        allprods.append([products, range(1,nSlides), nSlides])
    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        '''
            second argument of get is default value if first argument not present
        '''
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prViews(request,myid):
    # Fetching the products using id
    product = Product.objects.filter(id = myid)
    return render(request,'shop/prodViews.html',{'product':product[0]})
    # product[0] bcz product is in form of list. So to ease rendering we use product[0]

def checkout(request):
    return render(request,'shop/checkout.html')