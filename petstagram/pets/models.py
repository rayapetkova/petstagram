from django.db import models


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    personal_photo = models.URLField(
        null=False,
        blank=False
    )

    date_of_birth = models.DateField(
        null=False,
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True
    )