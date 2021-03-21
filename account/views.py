from django.shortcuts import render,HttpResponse,redirect
from django.contrib.messages import constants as messages
from django.contrib import messages

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from datetime import datetime, timedelta
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from webservices.scrapeitems.fetch import update_products
from webservices.scrapeitems.sales import get_sales
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from decimal import Decimal as D
from random import shuffle
from django.views import View
from .emails import welcome_mail
'''custom methods'''
from .custom_methods import *



'''views methods'''
def all_products(request):
    #update_products()
    items = Item.objects.all()
    items = list(items)
    shuffle(items)
    if request.method == 'POST':
            add_to_fav(request)
    brand_query = request.GET.get('brand_query',False)
    '''creating brand filter buttons'''
    brand_buttons = Item.objects.values_list('brand',flat=True).distinct()
    brand_buttons = set(brand_buttons)
    if brand_query:  
        items = Item.objects.filter(brand=brand_query)
        head = brand_query.upper()
    else:
        items = items
        head = "ALL PRODUCTS"
    page = Paginator(items,36)
    page_num = request.GET.get('page',1)
    try:
        page_items = page.page(page_num)
    except EmptyPage:
        page_items = page.page(1)
    context  = {
        'items': page_items,
        'brands':brand_buttons,
        'head':head,
        #filter-context
        'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),

        }
    
    return render(request,'all_products.html',context)

@login_required
def change_password(request):
    if request.method =="POST":
        if request.POST.get('change_btn'):
            new_password = request.POST.get('password1')
            request.user.set_password(new_password)
            request.user.save()
            
            return render('/login')
    return render(request,"change_password.html")


def contact(request):
    base = "baseRegistered.html"
        
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name = name, email = email, message= message, date= datetime.today())
        contact.save()
        messages.success(request,   'Your Message has been sent!')

    return render(request, "contact.html" ,{'base': base})

@login_required
def favorites(request):
    base = "baseRegistered.html"
    if request.method == 'POST':
        req_id = request.POST.get('product_id')
        Favorite.objects.filter(item_id = req_id).delete()
        messages.add_message(request, messages.ERROR,  'Item Removed Successfully!') 
    
    items = Favorite.objects.filter(owner=request.user).distinct()
    
    context = {
        'base':base,
        'items':items
    }
    return render(request, "favorites.html", context)


def filtered_items(request):
    items = Item.objects.all()
    items = list(items)
    shuffle(items)
    brand_query = request.GET.get('brand_query',False)
    '''creating brand filter buttons'''
    brand_buttons = Item.objects.values_list('brand',flat=True).distinct()
    brand_buttons = set(brand_buttons)
    if brand_query:  
        items = Item.objects.filter(brand=brand_query)
        head = brand_query.upper()
    else:
        items = items
        head = "ALL PRODUCTS"
    brands = None
    categories  = None
    if request.method == "POST":
        if request.POST.get('product_id'):
            add_to_fav(request)
        if request.POST.get('min'):
            price1 = D(request.POST.get('min')) 
            price2 = D(request.POST.get('max'))
            items = Item.objects.filter(price__range=(price1, price2))
            head = "Filtered Items"
        if request.POST.getlist('brand_filter'):
            brands = request.POST.getlist('brand_filter')
        if request.POST.getlist('cat_filter'):
            categories = request.POST.getlist('cat_filter')
        if brands and not categories:
            items = Item.objects.filter(price__range=(price1, price2), brand__in=brands)
        if categories and not brands:
            items = Item.objects.filter(price__range=(price1, price2), category__title__in=categories)
        if categories and brands:
            items = Item.objects.filter(price__range=(price1, price2), brand__in=brands,category__title__in=categories)
    
    
    # page = Paginator(items,36)
    # page_num = request.GET.get('page',1)
    # try:
    #     items = page.page(page_num)
    # except EmptyPage:
    #     items = page.page(1)
    context = {
        'items': items,
        'brands': brand_buttons,
        'head': head,
        #filter-context
        'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),

    }
    return render(request,"filtered_items.html", context)


def fragrances(request):
    base = "baseRegistered.html"
    if request.method == 'POST':
            add_to_fav(request)       
    PREF = Preferences.objects.get(title="Fragrances")
    items = Item.objects.filter(category=PREF).distinct()
    brand_buttons = Item.objects.filter(category=PREF).values_list('brand',flat=True).distinct()
    brand_buttons = set(brand_buttons)
    
    brand_query = request.GET.get('brand_query',False)
    if brand_query:  
        items = Item.objects.filter(brand=brand_query,category=PREF).distinct()
        head = brand_query.upper()
    else:
        head = "FRAGRANCES"
    context  = {
        'items': items,
        'base' : base,
        'brands':brand_buttons,
        'head':head,
        #filter-context
       'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),


        }
    return render(request,'fragrances.html',context)


def index(request):
    items = []
    head = ""
    if request.method == "POST":
        if request.POST.get('brand_button'):
            head = request.POST.get('brand_button')
            items = Item.objects.filter(brand=head)
        if request.POST.get('cat_button'):
            head = request.POST.get('cat_button')
            cat = Preferences.objects.get(title__iexact=head)
            #print(cat)
            items = Item.objects.filter(category=cat)
        context = {
            'items':items,
            'head': head,
            'pref': Preferences.objects.values_list('title',flat=True).distinct(),
            'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),
        }
        return render(request,'explore-items.html',context)
    context = {
        'pref': Preferences.objects.values_list('title',flat=True).distinct(),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),
        'type': Preferences.objects.values_list('pref_type',flat=True).distinct(),
    }
    return render(request, "index.html", context)


def loginUser(request):
    if request.method == "POST":
        #check user has entered vallid credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        requestingUser = authenticate(username=username, password=password)
        if requestingUser is not None:
            login(request,requestingUser)
            return redirect("/profile")
        messages.success(request,   'Oops! Username or Password is Invalid.')
    
    return render(request, "login.html")

@login_required
def logoutUser(request):
    logout(request)
    return redirect("/")   


def newarrival(request):
    #items = Item.objects.filter(datetime__gte=datetime.now()-timedelta(days=3))
    items = Item.objects.all().order_by('datetime').order_by('price')
    context = {'items':items,
        'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),

    }
    return render(request,"newarrival.html",context)   
@login_required
def preferences(request):
    base = "baseRegistered.html"
    prefered  = UserPreferences.objects.filter(user= request.user).distinct()
    items_list = []
    for item in prefered:
        items_list.append(item.category.title)
    if request.method == 'POST':
        categories = request.POST.getlist('item_type')
        UserPreferences.objects.filter(user=request.user).delete()
        for cat in categories:
            item_type = Preferences.objects.get(title=cat)
            UserPreferences(user=request.user, category=item_type).save()
            prefered  = UserPreferences.objects.filter(user= request.user).distinct()
            items_list = []
            for item in prefered:
                items_list.append(item.category.title)
    
    
    context = {
        'categories': Preferences.objects.all(), 
        'selected':items_list,
        'base':base
        }
    return render(request, "preferences.html", context)

@login_required
def profile(request):
    base = 'baseRegistered.html'
    brand_buttons = []
    '''loading profile'''
    items = get_prefered_items(request.user)
    if len(items)>0:
        items = get_prefered_items(request.user)
        flag = True
        prefered = UserPreferences.objects.filter(user=request.user)
        brand_buttons = []
        for cat in prefered:
            items = Item.objects.filter(category=cat.category).distinct()
            for item in items:
                brand_buttons.append(item.brand)    
        brand_buttons = set(brand_buttons)
    else:
        items = Item.objects.all().distinct()
        flag = False

    

    '''adding to favourites'''
    if request.method == 'POST':
            add_to_fav(request)
    '''handling filterations'''
    items_list = []
    '''creating filter buttons'''
    brand_query = request.GET.get('brand_query',False)
    if brand_query:
        items_list.clear()
        for cat in prefered:
            items = Item.objects.filter(brand=brand_query,category=cat.category).distinct()
            for item in items:
                items_list.append(item) 
        items = items_list 
    
    context = {
        'base' : base,
        'items': items,
        'flag':flag,
        'brands':brand_buttons,
        #filter-context
        'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
        'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),


    }
    return render(request, "profile.html",context)

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if len(Account.objects.filter(username=username)):
            messages.info(request,   'Username Alreadt Exists!')
            return redirect('/register')
        name     = request.POST.get('name')
        email = request.POST.get('email')
        if len(Account.objects.filter(email=email)):
            messages.info(request,   'Email is Already Registered!')
            return redirect('/register')
        contact = request.POST.get('contact')
        if len(Account.objects.filter(contact=contact)):
            messages.info(request,   'Contact Number is Already Registered!')
            return redirect('/register')
        password1 = request.POST.get('password')
        if len(password1)<8:
            messages.info(request,   'Password Must Contain atleast 8 Characters!')
            return redirect('/register')
        password2 = request.POST.get('confirm_password')
        if str(password1) !=str(password2):
            messages.info(request,   'Password does not match!')
            return redirect(request.path)
        new_user = Account(email = email,username = username,name = name, contact = contact,password = password1)
        welcome_mail(name,email)
        #Account.set_password(password1)
        login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/preferences')
    return render(request,'register.html')

def sales(request):
    #get_sales()
    #Sale.objects.all().delete()
    context = {
        'sales'  : Sale.objects.all(),
    }
    return render(request,"sales.html", context)
def search(request):
    try:
        search = request.GET.get('search')
    except:
        search = None
    
    base = "baseRegistered.html"
    
    if search:
        items = []
        flag = False
        suggestions = []
        if request.method == 'POST':
            add_to_fav(request)
        template = 'results.html'

        all_items = Item.objects.all()
        #search = search.split()
        # for token in search:
        #     i=SearchQuery(token) 
        #     items.append(i)
        
        #items = [item for item in all_items if search_matches(search,item) ]
        #tokens = search.split()
        # items = Item.objects.filter(title__in=tokens,brand__in=tokens,category__in=tokens)
        # for token in tokens:
        #     lookups= Q(title__icontains=token) | Q(category__icontains=token) | Q(brand__icontains=token)
        #     items += list(Item.objects.filter(lookups).distinct())
        items = Item.objects.annotate(search = SearchVector ('title', 'brand'),).filter(search = search)
        #items = Item.objects.filter(title__icontains=search,brand__icontains=search)
        # qs = Item.objects.all()
        # query = SearchQuery(search)
        # vector = SearchVector('title', 'brand','category')
        # qs = qs.annotate(search=vector).filter(search=query)
        # items = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        if len(items)<15:
            flag = True
            suggestions =list(Item.objects.all())
            shuffle(suggestions)
        page = Paginator(items,24)
        page_num = request.GET.get('page',1)
        try:
            page_items = page.page(page_num)
        except EmptyPage:
            page_items = page.page(1)
        context  = {
            'items': page_items,
            'count': len(items),
            'query': search,
            'flag': flag,
            'suggestions':suggestions,
            'base': base ,
            #filter-context
            'pref': set(Preferences.objects.values_list('title',flat=True).distinct()),
            'brands_list':set(Item.objects.values_list('brand', flat=True).distinct()),


            } 
        return render(request, template, context)      
    return redirect('/')


@login_required
def settings(request):
    if request.method == 'POST':
        if request.POST.get('update'):
            request.user.set_name(request.POST.get('name_input'))
            request.user.set_email(request.POST.get('email_input'))
            request.user.set_contact(request.POST.get('contact_input'))
            messages.success(request,'Settings Updated!')
        if request.POST.get('email_notification_input'):
            print("email input")
            request.user.set_email_notification()
        else:
            request.user.del_email_notification()
        if request.POST.get('sms_notification_input'):
            request.user.set_sms_notification()
        else:
            request.user.del_sms_notification()
        if request.POST.get('check_pass'):
            password = request.POST.get('old_password')
            #password = request.make_password(password)
            print(password)
            if request.user.check_password(password):
                return redirect('/change_password')
            else:
                messages.success(request,'You Entered an Invalid Password!')
    return render(request,'settings.html')






