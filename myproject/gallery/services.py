
import logging

from django.core.mail import send_mail

logger = logging.getLogger('gallery')


def send_upload_notification(instance):
    send_mail(
        subject='New image of the project.',
        message=(
            f'For project "{instance.project.title}" '
            'a new image has been uploaded.'
        ),
        from_email='admin@example.com',
        recipient_list=['owner@example.com']
    )


def write_log(message):
    logger.info(message)
