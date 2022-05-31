from django.db import models
from faker import Faker

import accounts.models


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

    @classmethod
    def generate_students(cls, count):
        faker = Faker()
        for _ in range(count):
            s = Student()
            s.profile = accounts.models.Profile.create_account()
            s.phone_number = faker.phone_number()

            s.save()
