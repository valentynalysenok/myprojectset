from django.contrib import admin

from .models import Project, Technology, Industry


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'company')
    list_per_page = 25


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title',)
    list_per_page = 25


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title',)
    list_per_page = 25
