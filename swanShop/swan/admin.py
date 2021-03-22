from django.contrib import admin
from .models import product,user,category,customer,orders


# Register your models here.
class adminproduct(admin.ModelAdmin):
    list_display=['pid','pname','price','category']

class admincategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(product,adminproduct)
admin.site.register(user)
admin.site.register(category,admincategory)
admin.site.register(customer)
admin.site.register(orders)