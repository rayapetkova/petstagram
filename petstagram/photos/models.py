from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


def validate_files_size(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0

    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size is {megabyte_limit}MB")


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False,
        validators=(validate_files_size,)
    )

    description = models.CharField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        null=True,
        blank=True
    )
