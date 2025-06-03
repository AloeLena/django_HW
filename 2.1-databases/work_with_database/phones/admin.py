from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date', 'lte_exists')

    list_filter = ('lte_exists',)

    search_fields = ('name', 'price')