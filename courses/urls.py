from django.urls import path

from courses.views import AllCoursesView

app_name = 'courses'

urlpatterns = [
    path('', AllCoursesView.as_view(), name='all_courses'),
    ]
