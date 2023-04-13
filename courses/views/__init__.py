# from django.contrib.auth.mixins import LoginRequiredMixin

from .common import IndexTemplateView
from .course import (
    CourseCreateView,
    CourseListView,
    CourseDeleteView,
    CourseDetailView,
    CourseUpdateView,
)
