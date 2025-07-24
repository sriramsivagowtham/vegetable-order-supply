from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from .models import Post
from django.http import Http404
from .forms import CustomerUserForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import DashForm

import uuid





#------------------ #register-------------------------------------
def index_view(request): 
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()                                 
            return redirect('/dashboard')
        else:
            print("error in rigister form:",form.errors) 
    else:
        form = CustomerUserForm()

    return render(request, 'index.html', {'form': form})

#---------login------------------------------------------------------
def login_views(request):
    return render(request,'login.html')


def login_view(request):
    form = AuthenticationForm()
    if request.method =='POST':
        values = AuthenticationForm(request, data=request.POST)
        if values.is_valid():
            username = values.cleaned_data.get('username')
            password = values.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form': form})
        

#-----------------logout----------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('/index')                    #in header logout formula


#-------------------------detail--page----------------------------------------------
# @login_required(login_url='/index')
def detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})
#________________admin_______menu_______________________
# @login_required(login_url='/index')
def menu_view(request):
    Veg_title="Vegetables Available List"
    poste=Post.objects.all()
    return render(request,'menu.html',{'Veg_title':Veg_title, 'poste':poste})

#-------------------vegetable -----------------------------------------
def order_page(request):
    return render(request,'orderplace.html')

from .models import CustomerOrder, VegetableItem

def vegetable_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        veg_names = request.POST.getlist('veg_name[]')
        veg_prices = request.POST.getlist('veg_price[]')
        veg_kgs = request.POST.getlist('veg_kg[]')

        # Create customer order
        customer_order = CustomerOrder.objects.create(customer_name=customer_name)

        total = 0
        for name, price, kg in zip(veg_names, veg_prices, veg_kgs):
            price = float(price)
            kg = float(kg)
            amount = price * kg
            total += amount
            VegetableItem.objects.create(
                customer_order=customer_order,
                veg_name=name,
                veg_price=price,
                veg_kg=kg,
                amount=amount
            )

        customer_order.total_amount = total
        customer_order.save()
        return redirect('/success')  
    return render(request,'orderplace.html')   



#----------------Order--success---------------------------
# @login_required(login_url='/index',redirect_field_name='first login or register')
def order_views(request):
    return render(request,'submit.html')
#____________________dashboar__ or__about_page___________

# @login_required(login_url='/index')
def dashboard_view(request):
    if request.method == 'POST':
        form = DashForm(request.POST)
        if form.is_valid():
            form.save()                                 
            return redirect('/order')
        else:
            print("Error in about form", form.errors) 
    else:
        form = DashForm()

    return render(request, 'dashboard1.html', {'go_to_order': form})

    





