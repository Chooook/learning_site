
# class StudentCreateView(CreateView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
#     form_class = StudentForm
#
#
# class StudentListView(ListView):
#     model = Student
#     context_object_name = 'student_list'
#
#
# class StudentDetailView(DetailView):
#     model = Student
#
#
# class StudentUpdateView(UpdateView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
#     form_class = StudentForm
#
#
# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = reverse_lazy('courses:student-list')
