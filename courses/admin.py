from django.contrib import admin

from .models import Theme, Course, Teacher, Student


@admin.register(Theme)
class ThemeModelAdmin(admin.ModelAdmin):
    list_display = ('theme_name', 'description')


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'about_course', 'display_studied_themes')

    def display_studied_themes(self, obj):
        themes = obj.studied_themes.values_list('theme_name', flat=True)
        return '; '.join(themes)
    display_studied_themes.short_description = 'studied_themes'


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'patronymic_name',
        'birth_date', 'display_competences', 'display_courses'
    )

    def display_competences(self, obj):
        competences = obj.competences.values_list('theme_name', flat=True)
        return '; '.join(competences)
    display_competences.short_description = 'competences'

    def display_courses(self, obj):
        courses = obj.taught_courses.values_list('course_name', flat=True)
        return '; '.join(courses)
    display_courses.short_description = 'taught_courses'


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'patronymic_name', 'birth_date',
        'display_studied_courses', 'display_current_courses'
    )

    def display_studied_courses(self, obj):
        studied_courses = obj.studied_courses.values_list(
            'course_name', flat=True
        )
        return '; '.join(studied_courses)
    display_studied_courses.short_description = 'studied_courses'

    def display_current_courses(self, obj):
        current_courses = obj.current_courses.values_list(
            'course_name', flat=True
        )
        return '; '.join(current_courses)
    display_current_courses.short_description = 'current_courses'
