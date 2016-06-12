# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import OfficialDealer, Detail, CarModel, Car, CarDetail

class OfficialDealerAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class CarAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class CarDetailAdmin(admin.ModelAdmin):
    list_display = ('name','name')

admin.site.register(OfficialDealer, OfficialDealerAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarDetail, CarDetailAdmin)
