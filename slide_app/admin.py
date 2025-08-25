from django.contrib import admin
from .models import *
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    fieldsets = [
        ['General information',{'fields':['title', 'image']}],
        ]
    
    list_display = ('id','title')