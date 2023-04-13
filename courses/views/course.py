from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from .. import models, forms


class CourseCreateView(CreateView):
    model = models.Course
    success_url = reverse_lazy('courses:course-list')
    form_class = forms.CourseForm


class CourseListView(ListView):
    model = models.Course
    context_object_name = 'course_list'


class CourseDetailView(DetailView):
    model = models.Course


class CourseUpdateView(UpdateView):
    model = models.Course
    success_url = reverse_lazy('courses:course-list')
    form_class = forms.CourseForm


class CourseDeleteView(DeleteView):
    model = models.Course
    success_url = reverse_lazy('courses:course-list')
