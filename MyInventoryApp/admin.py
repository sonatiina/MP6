from django.contrib import admin

# Register your models here.
from .models import Supplier
from .models import WaterBottle
admin.site.register(Supplier)
admin.site.register(WaterBottle)
