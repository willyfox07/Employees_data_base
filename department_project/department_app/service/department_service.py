
import requests
from django.http import JsonResponse
from ..models.department import Department
from department_app.forms.department_form import DepartmentForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,\
                                    ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from rest_framework.reverse import reverse

class DepartmentListView(ListView):
    """Class for dispalying models"""
    model = Department
    template_name = 'department_page.html'
    context_object_name = 'Department'
    object_list = None

    def get_context_data(self, **kwargs):
        department = requests.get(reverse('department_api', request=self.request)).json()
        context = MultipleObjectMixin.get_context_data(self, **kwargs)
        context['Department'] = department
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        params = request.GET
        min = params.get('min', '')
        max = params.get('max', '')
        location = params.get('location', '')
        filter_department = '?min=' + min + '&max=' + max + '&location=' + location
        department = requests.get(reverse('department_api', request=self.request) + filter_department).json()
        context['Department'] = department
        return self.render_to_response(context)


class DepartmentCreateView(CreateView):
    """Class for creating new model"""
    model = Department
    template_name = 'add_department.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('department_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Department'] = Department.objects.all()
        return context


class DepartmentUpdateView(UpdateView):
    """class for editing the model"""
    model = Department
    template_name = 'edit_department.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('department_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Department'] = Department.objects.all()
        return context


class DepartmentDeleteView(DeleteView):
    """Class for deleting model"""
    model = Department
    success_url = reverse_lazy('department_page')