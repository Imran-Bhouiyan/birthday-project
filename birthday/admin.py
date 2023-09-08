from django.contrib import admin

# Register your models here.
from .models import * 



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email'
                
   
    )
    list_filter = (
         'id',
        'full_name',
        'email'
               
     
    )
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
                
   
    )
    list_filter = (
         'id',
        'customer',
               
     
    )
    