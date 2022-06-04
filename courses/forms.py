from django.forms import ModelForm, Form, FileField, ClearableFileInput

from courses.models import Lesson


class LessonCreateForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class FileFieldForm(Form):
    file_field = FileField(required=False, widget=ClearableFileInput(attrs={'multiple': True}))
