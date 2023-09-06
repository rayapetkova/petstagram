from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    comment_text = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )

    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True
    )

    relation_to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )


class Like(models.Model):
    relation_to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
