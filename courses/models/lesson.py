from django.db import models

from core_lms.models.material import Material


class Lesson(Material):
    planned_time = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(to='courses.Course', on_delete=models.CASCADE,
                               related_name='lessons')
