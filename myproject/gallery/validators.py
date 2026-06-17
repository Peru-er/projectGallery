
from django.core.exceptions import ValidationError
from PIL import Image


def validate_image(file):
    try:
        image = Image.open(file)
        image.verify()
    except Exception:
        raise ValidationError('File is not image.')

def validate_min_size(file):
    image = Image.open(file)

    if image.width < 300 or image.height < 200:
        raise ValidationError(
            'Minimum size: 300x200.'
        )

def validate_exif(file):
    image = Image.open(file)

    exif = image.getexif()

    forbidden_tags = [
        'UserComment',
        'XPComment'
    ]

    for tag_id, value in exif.items():
        tag = Image.ExifTags.TAGS.get(tag_id)

        if tag in forbidden_tags:
            raise ValidationError(
                'Suspicious EXIF data.'
            )


validate_image()
validate_min_size()
validate_exif()
