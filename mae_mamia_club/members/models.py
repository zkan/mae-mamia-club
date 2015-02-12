from django.db import models


class Member(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    birthdate = models.DateField(
        null=True,
        blank=True
    )

    dad_name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    mom_name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    signup_date = models.DateField(
        null=True,
        blank=True,
        auto_now_add=True
    )
