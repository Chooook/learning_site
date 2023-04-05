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

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic_name = models.CharField(max_length=32, default='')
    birth_date = models.DateField()
    about_me = models.TextField(default='')


class Theme(models.Model):
    theme_name = models.CharField(unique=True, max_length=64)
    description = models.TextField()


class Course(models.Model):  # стоит подумать о сущности Потока
    course_name = models.CharField(unique=True, max_length=256)
    about_course = models.TextField()
    studied_themes = models.ManyToManyField(
        Theme, related_name='courses_on_theme'
    )


class Teacher(PersonMixin):
    competences = models.ManyToManyField(Theme, related_name='theme_teachers')
    taught_courses = models.ManyToManyField(
        Course, related_name='course_teachers'
    )


class Student(PersonMixin):
    studied_courses = models.ManyToManyField(
        Course, related_name='students_passed'
    )
    courses_to_be_studied = models.ManyToManyField(
        Course, related_name='students_current'
    )

# TODO добавить модели Расписания и Урока
