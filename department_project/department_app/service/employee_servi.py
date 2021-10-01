import requests

from department_app.models.employee import Employees
from django.urls import reverse_lazy
from department_app.forms.employee_form import EmployeeForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from department_app.service.department_service import DepartmentListView
from rest_framework.reverse import reverse

class EmployeeListView(ListView):
    """Class for dispalying models"""
    model = Employees
    template_name = 'employee_page.html'
    context_object_name = 'Employees'
    object_list = None

    def get(self, request, *args, **kwargs):
        """Function for filtering requested data"""
        context = self.get_context_data(**kwargs)
        params = request.GET
        date_from = params.get('date_from', '')
        date_to = params.get('date_to', '')
        department = params.get('department', '')
        employee_filter = '?date_from=' + date_from + '&date_to=' + date_to + '&department=' + department
        employee = requests.get(reverse('employee_api', request=self.request) + employee_filter).json()
        context['Employees'] = employee
        return self.render_to_response(context)


class EmployeeCreateView(CreateView):
    """Class for creating new model"""
    model = Employees
    template_name = 'add_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Employees'] = Employees.objects.all()
        return context


class EmployeeUpdateView(UpdateView):
    """class for editing the model"""
    model = Employees
    template_name = 'edit_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_page')


class EmployeeDeleteView(DeleteView):
    """class for deleting the model"""
    model = Employees
    success_url = reverse_lazy('employee_page')