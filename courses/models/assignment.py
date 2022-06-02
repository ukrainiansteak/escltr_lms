from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(to='courses.Course', on_delete=models.CASCADE,
                               related_name='assignments')
