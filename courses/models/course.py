from PIL import Image
from django.core.validators import FileExtensionValidator
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
    cover = models.ImageField(
        null=True,
        upload_to='covers/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png', 'jpeg'])
        ])

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        if self.cover:
            cover = self.cover
            with Image.open(cover) as im:
                width = 640
                height = 360
                path = self.cover.path
                self.cover = im.resize((width, height), Image.ANTIALIAS)
                self.cover.save(path)
