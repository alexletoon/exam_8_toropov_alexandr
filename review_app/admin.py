from django.contrib import admin
from review_app.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created_at',]
    list_filter = ['id', 'name', 'category', 'created_at']
    search_fields=['id', 'name', 'category', 'created_at']
    fields= ['name', 'category', 'image','description']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'rating', 'created_at',]
    list_filter = ['id', 'author', 'product', 'rating', 'created_at',]
    search_fields=['id', 'author', 'product', 'rating', 'created_at',]
    fields= ['author', 'product', 'rating','text']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)