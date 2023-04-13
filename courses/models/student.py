from django.db import models

from courses.models.course import Course
from courses.models.mixins import PersonMixin


class Student(PersonMixin):
    studied_courses = models.ManyToManyField(
        Course, related_name='students_passed',
        blank=True, help_text='Пройденные курсы.'
    )
    current_courses = models.ManyToManyField(
        Course, related_name='students_current',
        blank=True, help_text='Текущие курсы.'
    )

    class Meta:
        app_label = 'courses'
