from django.contrib import admin
from .models import Recepie

class ListingRecepies(admin.ModelAdmin):
    list_display = ('id', 'recepie_name', 'category', 'prepare_time', 'is_published')
    list_display_links = ('id', 'recepie_name')
    search_fields = ('recepie_name', )
    list_filter = ('category',)
    list_editable = ('is_published',)
    list_per_page = 10

admin.site.register(Recepie, ListingRecepies)
