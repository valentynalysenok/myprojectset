from django.contrib import admin

from .models import Company, Review


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'hourly_rate', 'employees', 'website')
    list_filter = ('created',)
    search_fields = ('title', 'hourly_rate')
    list_per_page = 25


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('company', 'user')
    list_per_page = 25
