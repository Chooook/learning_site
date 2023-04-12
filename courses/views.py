# from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    # FormView,
    UpdateView,
    DeleteView
)

from .forms import (
    CourseForm,
    # ThemeForm, TeacherForm, StudentForm
)
from .models import (
    Course,
    # Theme, Teacher, Student
)


class IndexTemplateView(TemplateView):
    template_name = 'courses/index.html'


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('courses:course-list')
    form_class = CourseForm


class CourseListView(ListView):
    model = Course
    context_object_name = 'course_list'


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:course-list')
    form_class = CourseForm


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:course-list')


# class ThemeCreateView(CreateView):
#     model = Theme
#     success_url = reverse_lazy('courses:theme-list')
#     form_class = ThemeForm
#
#
# class ThemeListView(ListView):
#     model = Theme
#     context_object_name = 'theme_list'
#
#
# class ThemeDetailView(DetailView):
#     model = Theme
#
#
# class ThemeUpdateView(UpdateView):
#     model = Theme
#     success_url = reverse_lazy('courses:theme-list')
#     form_class = ThemeForm
#
#
# class ThemeDeleteView(DeleteView):
#     model = Theme
#     success_url = reverse_lazy('courses:theme-list')


# class TeacherCreateView(CreateView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')
#     form_class = TeacherForm
#
#
# class TeacherListView(ListView):
#     model = Teacher
#     context_object_name = 'teacher_list'
#
#
# class TeacherDetailView(DetailView):
#     model = Teacher
#
#
# class TeacherUpdateView(UpdateView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')
#     form_class = TeacherForm
#
#
# class TeacherDeleteView(DeleteView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')


# class StudentCreateView(CreateView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
#     form_class = StudentForm
#
#
# class StudentListView(ListView):
#     model = Student
#     context_object_name = 'student_list'
#
#
# class StudentDetailView(DetailView):
#     model = Student
#
#
# class StudentUpdateView(UpdateView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
#     form_class = StudentForm
#
#
# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
