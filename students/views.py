from django.views.generic import ListView

from students.models import Student


class AllStudentsView(ListView):
    model = Student
    template_name = 'all_students.html'
    queryset = Student.objects.all()
