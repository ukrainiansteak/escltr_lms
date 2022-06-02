from django.views.generic import ListView, DetailView

from courses.models import Course


class AllCoursesView(ListView):
    model = Course
    template_name = 'all_courses.html'
    queryset = Course.objects.all()


class CourseView(DetailView):
    model = Course
    pk_url_kwarg = 'id'
    template_name = 'course.html'
