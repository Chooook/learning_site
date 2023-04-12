from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('',
         views.IndexTemplateView.as_view(),
         name='index'),
    path('course/create',
         views.CourseCreateView.as_view(),
         name='course-create'),
    path('course/list',
         views.CourseListView.as_view(),
         name='course-list'),
    path('course/detail/<int:pk>',
         views.CourseDetailView.as_view(),
         name='course-detail'),
    path('course/update/<int:pk>',
         views.CourseUpdateView.as_view(),
         name='course-update'),
    path('course/delete/<int:pk>',
         views.CourseDeleteView.as_view(),
         name='course-delete'),
]
