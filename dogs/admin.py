from django.contrib import admin
from dogs.models import Dog,Categories

@admin.register(Dog)
class Dog(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('categories',)

@admin.register(Categories)
class Dog(admin.ModelAdmin):
    list_display = ('name',)
