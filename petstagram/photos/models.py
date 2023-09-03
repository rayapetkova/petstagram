from django.core.validators import MinLengthValidator
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        null=False,
        blank=False
    )

    location = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True
    )