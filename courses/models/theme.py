from django.db import models


class Theme(models.Model):
    theme_name = models.CharField(
        unique=True, max_length=64, help_text='Название темы'
    )
    description = models.TextField(help_text='Описание темы')

    def __str__(self):
        return self.theme_name

    class Meta:
        app_label = 'courses'
