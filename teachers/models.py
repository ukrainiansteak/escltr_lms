from django.db import models
from faker import Faker

import accounts.models


class Teacher(models.Model):
    profile = models.OneToOneField(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name="teacher"
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

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()
        for _ in range(count):
            t = Teacher()
            t.profile = accounts.models.Profile.create_account()
            t.phone_number = faker.phone_number()

            t.save()
