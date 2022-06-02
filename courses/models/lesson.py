from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    planned_time = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(to='courses.Course', on_delete=models.CASCADE,
                               related_name='lessons')
