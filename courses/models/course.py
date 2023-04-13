from django.db import models

from courses.models.theme import Theme


class Course(models.Model):  # стоит подумать о сущности Потока
    course_name = models.CharField(
        unique=True, max_length=256, help_text='Название курса'
    )
    about_course = models.TextField(help_text='Описание курса')
    studied_themes = models.ManyToManyField(
        Theme, related_name='courses_on_theme',
        help_text='Темы, рассматриваемые в курсе.'
    )

    def __str__(self):
        return self.course_name

    class Meta:
        app_label = 'courses'
