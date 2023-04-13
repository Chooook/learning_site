from django.db import models

from courses.models.course import Course
from courses.models.mixins import PersonMixin
from courses.models.theme import Theme


class Teacher(PersonMixin):
    competences = models.ManyToManyField(
        Theme, related_name='theme_teachers',
        help_text='Компетенции преподавателя.'
    )
    taught_courses = models.ManyToManyField(
        Course, related_name='course_teachers', blank=True,
        help_text='Курсы, в которых преподаватель задействован.'
    )

    class Meta:
        app_label = 'courses'
