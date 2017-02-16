from django.contrib import admin
from main.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price','created', 'updated']
	list_filter = ['created', 'updated', 'name']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

