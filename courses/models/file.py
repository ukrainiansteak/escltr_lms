from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class File(models.Model):
    file = models.FileField(
        upload_to='files/',
        validators=[
            FileExtensionValidator(['jpg', 'png', 'jpeg', 'gif', 'pdf', 'doc',
                                    'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt',
                                    'mp3', 'm4a', 'wav', 'mp4', 'mov', 'avi',
                                    'mpeg', 'mpg', 'wmv', 'swf', 'epub', 'mobi',
                                    'fb2', 'xml'])
        ]
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     related_name='files')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]