
from django.db import models
from .validators import (
    validate_image,
    validate_min_size,
    validate_exif
)


class Project(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    original_image = models.ImageField(
        upload_to='gallery/original/',
        validators=[
            validate_image,
            validate_min_size,
            validate_exif
        ]
    )
    thumbnail = models.ImageField(upload_to='gallery/thumbs/', blank=True)
    medium_image = models.ImageField(upload_to='gallery/medium/', blank=True)
    large_image = models.ImageField(upload_to='gallery/large/', blank=True)
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.project.title



