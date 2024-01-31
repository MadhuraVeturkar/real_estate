from django.contrib import admin
from .models import Properties, Contact

# Register your models here.
admin.site.register(Contact)

# TO Modify Properties view for admin
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title','property_type','property_status','price','area']
    list_filter = ('property_type','property_status')
admin.site.register(Properties, PropertyAdmin)