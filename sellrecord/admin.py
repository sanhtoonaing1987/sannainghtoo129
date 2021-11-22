from django.contrib import admin
from .models import Sellrecord

admin.site.site_header = 'Waaneiza Management System'

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','price','purchased_items','showroom','paid','date']
    list_filter = ['customer_name','customer_phone','price','purchased_items','showroom','paid','date']
    search_fields = ['customer_name','customer_phone','price','purchased_items','showroom','paid','date']
    
    

admin.site.register(Sellrecord, SellrecordAdmin) 