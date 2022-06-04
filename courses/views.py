from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from courses.forms import LessonCreateForm, FileFieldForm
from courses.models import Course, File


class AllCoursesView(ListView):
    model = Course
    template_name = 'all_courses.html'
    queryset = Course.objects.all()


class CourseView(DetailView):
    model = Course
    pk_url_kwarg = 'id'
    template_name = 'course.html'


class CreateLessonView(View):

    def get(self, request, *args, **kwargs):
        lesson_form = LessonCreateForm
        file_form = FileFieldForm

        return render(
            request,
            'create_lesson.html',
            context={
                'lesson_form': lesson_form,
                'file_form': file_form,
            },
        )


    def post(self, request, *args, **kwargs):
        form = LessonCreateForm(
            data=request.POST,
            )
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            form.save()
            for file in files:
                f = File()
                f.file = file
                f.content_type = ContentType.objects.get(app_label='courses', model='lesson')
                f.object_id = form.instance.id
                f.save()
            return redirect(reverse('courses:all_courses'))

