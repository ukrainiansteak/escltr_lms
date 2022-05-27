from django.db import models


class Student(models.Model):
    profile = models.OneToOneField(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone_number = models.CharField(
        null=True,
        max_length=24,
    )
    linkedin_profile = models.CharField(
        null=True,
        blank=True,
        max_length=150
    )
