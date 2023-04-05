from django.db import models
# from django.utils.functional import cached_property


class TimestampMixin(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(name='updated_at', auto_now=True)


class PersonMixin(models.Model):

    class Meta:
        abstract = True

    last_name = models.CharField(max_length=32, help_text='Фамилия')
    first_name = models.CharField(max_length=32, help_text='Имя')
    patronymic_name = models.CharField(
        max_length=32, default='', blank=True, help_text='Отчество'
    )
    birth_date = models.DateField(help_text='Дата рождения')
    about_me = models.TextField(
        default='', blank=True, help_text='Расскажите о себе'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Theme(models.Model):
    theme_name = models.CharField(
        unique=True, max_length=64, help_text='Название темы'
    )
    description = models.TextField(help_text='Описание темы')

    def __str__(self):
        return self.theme_name


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


class Teacher(PersonMixin):
    competences = models.ManyToManyField(
        Theme, related_name='theme_teachers',
        help_text='Компетенции преподавателя.'
    )
    taught_courses = models.ManyToManyField(
        Course, related_name='course_teachers',
        blank=True, help_text='Курсы, в которых преподаватель задействован.'
    )


class Student(PersonMixin):
    studied_courses = models.ManyToManyField(
        Course, related_name='students_passed',
        blank=True, help_text='Пройденные курсы.'
    )
    current_courses = models.ManyToManyField(
        Course, related_name='students_current',
        blank=True, help_text='Текущие курсы.'
    )

# TODO добавить модели Расписания и Урока
