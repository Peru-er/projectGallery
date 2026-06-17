
from django.contrib import admin

from .models import Project, ProjectGallery


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project',
        'uploaded_at'
    ]
