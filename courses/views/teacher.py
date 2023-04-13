
# class TeacherCreateView(CreateView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')
#     form_class = TeacherForm
#
#
# class TeacherListView(ListView):
#     model = Teacher
#     context_object_name = 'teacher_list'
#
#
# class TeacherDetailView(DetailView):
#     model = Teacher
#
#
# class TeacherUpdateView(UpdateView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')
#     form_class = TeacherForm
#
#
# class TeacherDeleteView(DeleteView):
#     model = Teacher
#     success_url = reverse_lazy('courses:teacher-list')
