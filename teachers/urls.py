from django.urls import path

from teachers.views import AllTeachersView

app_name = 'teachers'

urlpatterns = [
    path('', AllTeachersView.as_view(), name='all_teachers'),
    ]
