from PIL import Image
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from faker import Faker


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, avatar, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, avatar, is_admin, password=None):
        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            is_admin=is_admin,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Profile(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        unique=True
    )
    avatar = models.ImageField(
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png', 'jpeg'])
        ]
    )
    objects = UserManager()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.avatar:
            with Image.open(self.avatar) as im:
                if self.avatar.width > self.avatar.height:
                    width = 300
                    height = round(self.avatar.height * (width / self.avatar.width))
                elif self.avatar.width < self.avatar.height:
                    height = 300
                    width = round(self.avatar.width * (height / self.avatar.height))
                else:
                    width = 300
                    height = 300
                path = self.avatar.path
                self.avatar = im.resize((width, height), Image.ANTIALIAS)
                self.avatar.save(path)

    @classmethod
    def create_account(cls, count=1):
        faker = Faker()
        for _ in range(count):
            p = Profile()
            p.email = faker.email()
            p.username = p.email
            p.first_name = faker.first_name()
            p.last_name = faker.last_name()
            p.password = faker.password(length=20)

            p.save()
            return p
