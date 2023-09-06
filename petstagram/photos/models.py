from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_files_size


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

    liked_by_user = models.BooleanField(
        default=False,
        null=False,
        blank=True
    )
