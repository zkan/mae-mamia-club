from django.db import models


class Word(models.Model):
    text = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )
