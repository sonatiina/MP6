from django.shortcuts import render
from .models import WaterBottle, Supplier

# Create your views here.
def hello_world(request):
    return render(request, 'MyInventoryApp/hello_world.html')

def base(request):
    return render(request, 'MyInventoryApp/base.html')

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

def view_supplier(request):
    supplier = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {'supplier' : supplier})

def view_bottles(request):
    water_bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'water_bottles': water_bottles})