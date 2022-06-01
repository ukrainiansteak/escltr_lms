from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    students = models.ManyToManyField(to='students.Student',
                                      related_name='courses',
                                      )
    teachers = models.ManyToManyField(to='teachers.Teacher',
                                      related_name='courses'
                                      )
