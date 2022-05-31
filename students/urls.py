from django.urls import path

from students.views import AllStudentsView

app_name = 'students'

urlpatterns = [
    path('', AllStudentsView.as_view(), name='all_students'),
    ]
