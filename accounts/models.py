from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


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
            FileExtensionValidator(['jpg', 'png'])
        ]
    )
    objects = UserManager()
