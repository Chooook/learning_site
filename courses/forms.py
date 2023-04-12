from django import forms
# from django.core.exceptions import ValidationError

from .models import (
    Course,
    Theme,
    # Teacher, Student
)


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('course_name', 'about_course', 'studied_themes')

    course_name = forms.CharField(label='Course name')
    about_course = forms.CharField(
        label='Course description',
        widget=forms.Textarea
    )
    studied_themes = forms.ModelMultipleChoiceField(
        label='',
        queryset=Theme.objects.all(),
        widget=forms.SelectMultiple,
        required=False  # TODO УБРАТЬ ПОСЛЕ СОЗДАНИЯ ФОРМЫ Theme
    )

