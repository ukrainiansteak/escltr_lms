from django.db import models

from core_lms.models import Material


class Post(Material):
    author = models.ForeignKey(to='accounts.Profile', on_delete=models.SET_NULL,
                               related_name='posts', null=True)
