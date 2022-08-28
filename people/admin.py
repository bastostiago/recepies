from django.contrib import admin
from .models import People

class ListingPeople(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')

admin.site.register(People, ListingPeople)
