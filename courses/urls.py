from django.urls import path

from courses.views import AllCoursesView, CourseView

app_name = 'courses'

urlpatterns = [
    path('', AllCoursesView.as_view(), name='all_courses'),
    path('<int:id>', CourseView.as_view(), name='course'),
    ]
