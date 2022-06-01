from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.urls import reverse_lazy

from students.models import Student
from teachers.models import Teacher


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email")


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.replace(
                '../password/', kwargs.pop(reverse_lazy(
                    'accounts:change_password'), './password')
            )


class StudentProfileEditForm(ModelForm):
    class Meta:
        model = Student
        fields = ['phone_number', 'linkedin_profile']


class TeacherProfileEditForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['phone_number', 'linkedin_profile']
