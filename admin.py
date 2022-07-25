from django.contrib import admin
from mycar import models
from mycar.models import Car,Owner,Order

# Register your models here.
#admin.site.register(Car)
#admin.site.register(Owner)
#admin.site.register(Order)


class MyCarAdmin(admin.ModelAdmin):
    model = models.Car
    list_display = [
        
        "model_name",
        "model_num",
        "prize"
        
    ]
   # list_editable=[
        
    #    "model_name",
     #   "model_num",
     #   "prize"
       
    #]

class MyOwnerAdmin(admin.ModelAdmin):
        model = models.Owner
        list_display = [
        "name",
        "mobile",
    ]


class MyOrderAdmin(admin.ModelAdmin):
    model = models.Order
    list_display = [
        
        "owner",
        "car",
        "unit"
        
    ]




admin.site.register(models.Car,MyCarAdmin)
admin.site.register(models.Owner,MyOwnerAdmin)
admin.site.register(models.Order,MyOrderAdmin)