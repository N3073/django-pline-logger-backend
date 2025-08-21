from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ProductionLine)
class ProductionLineAdmin(admin.ModelAdmin):
    fieldsets = [
        ['General information',{'fields':['id','short_name', 'long_name']}],
        ]
    
    list_display = ('short_name','id','long_name')

@admin.register(LogData)
class LogDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ['General information',{'fields':['production_line','data_name', 'data_field', 'time_of_creation','sender_ip']}],
        ]
    
    list_display = ('production_line','data_name', 'data_field', 'time_of_creation','sender_ip')

@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ['General information',{'fields':['production_line','message_type', 'message_text', 'time_of_creation','sender_ip']}],
        ]
    
    list_display = ('production_line','message_type', 'message_text', 'time_of_creation','sender_ip')