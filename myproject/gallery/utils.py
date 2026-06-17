from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile


def remove_exif(img):

    data = list(img.getdata())

    clean_img = Image.new(
        img.mode,
        img.size
    )

    clean_img.putdata(data)

    return clean_img


def create_image(image_field, size):

    img = Image.open(image_field)

    clean_img = remove_exif(img)

    clean_img.thumbnail(size)

    output = BytesIO()

    clean_img.save(
        output,
        format='JPEG'
    )

    return ContentFile(output.getvalue())
