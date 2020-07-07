from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Project, Technology, Industry
from .resources import ProjectResource


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('title', 'company', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'company')
    resource_class = ProjectResource
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
