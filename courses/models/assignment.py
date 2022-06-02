from django.db import models

from core_lms.models.material import Material


class Assignment(Material):
    due_date = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(to='courses.Course', on_delete=models.CASCADE,
                               related_name='assignments')
