from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Material(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    files = GenericRelation('courses.File')
