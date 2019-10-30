from django.contrib import admin
from .models import Book, Category, Client, Rental
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Rental)