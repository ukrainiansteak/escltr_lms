from django.views.generic import ListView

from teachers.models import Teacher


class AllTeachersView(ListView):
    model = Teacher
    template_name = 'all_teachers.html'
    queryset = Teacher.objects.all()
