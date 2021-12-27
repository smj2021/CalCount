from django.contrib import admin
from .models import *

# Register your models here.
class foodAdmin(admin.ModelAdmin):
    class Meta:
        model=Fooditem
    list_display=['name']
    list_filter=['name']
    