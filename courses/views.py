from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course


class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy()


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass


class CourseDeleteMixin(OwnerCourseEditMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'


# class ManageCourseList(ListView):
#     model = Course
#     template_name = 'courses/manage/course/list.html'

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(owner=self.request.user)
