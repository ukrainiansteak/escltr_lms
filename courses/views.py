from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from courses.forms import LessonCreateForm, FileFieldForm
from courses.models import Course


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

    # todo: define post method

    # def post(self, request, *args, **kwargs):
    #     lesson_form = LessonCreateForm(
    #         data=request.POST,
    #         )
    #     file_form = FileFieldForm(
    #         files=request.FILES
    #     )
    #
    #     return render(
    #         request,
    #         'create_lesson.html',
    #         context={
    #             'lesson_form': lesson_form,
    #             'file_form': file_form,
    #         },
    #     )
    # success_url = ''
    #
    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('file_field')
    #     if form.is_valid():
    #         for f in files:
    #             ...  # Do something with each file.
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # pass
