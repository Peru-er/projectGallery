
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import ProjectGallery
from .utils import create_image

logger = logging.getLogger('gallery')


@receiver(post_save, sender=ProjectGallery)
def process_gallery(sender, instance, created, **kwargs):

    if not created:
        return

    logger.info(
        f'New image: {instance.original_image.name}'
    )

    instance.alt_text = (
        f'Project image {instance.project.title}'
    )

    # thumbnail
    thumb = create_image(instance.original_image, (150, 150))
    instance.thumbnail.save(
        'thumb.jpg',
        thumb,
        save=False
    )

    medium = create_image(instance.original_image, (600, 400))
    instance.medium_image.save(
        'medium.jpg',
        medium,
        save=False
    )

    large = create_image(instance.original_image, (1200, 800))
    instance.large_image.save(
        'large.jpg',
        large,
        save=False
    )

    instance.save()

    logger.info('All sizes successfully created.')

    send_mail(
        subject='New image of the project.',
        message=(
            f'For project "{instance.project.title}" '
            'a new image has been uploaded.'
        ),
        from_email='admin@example.com',
        recipient_list=['owner@example.com']
    )

    logger.info('Email sent.')
