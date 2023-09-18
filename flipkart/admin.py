from django.contrib import admin
from . models import Signup
from.models import Category
from .models import product
from .models import login1
from . models import Order
# Register your models here.
admin.site.register(Signup)
admin.site.register(Category)
admin.site.register(product)
admin.site.register(login1)
admin.site.register(Order)