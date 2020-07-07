from import_export import fields
from import_export import resources

from .models import Project


class ProjectResource(resources.ModelResource):
    company = fields.Field(attribute='company__title', column_name='company')

    class Meta:
        model = Project
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        fields = ('title', 'url', 'company',
                  'technologies', 'industries',
                  'description', 'notes')
        export_order = ('title', 'url', 'company',
                        'technologies', 'industries',
                        'description', 'notes')
        widgets = {'technologies': {'field': 'title'},
                   'industries': {'field': 'title'}}
