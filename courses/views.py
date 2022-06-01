from django.views.generic import ListView

from courses.models import Course


class AllCoursesView(ListView):
    model = Course
    template_name = 'all_courses.html'
    queryset = Course.objects.all()
