from django.db import models


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
