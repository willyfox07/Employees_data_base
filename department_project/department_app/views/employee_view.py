"""Module for control serializers of employee models"""
from rest_framework import generics
from ..rest.employee_serializer import EmployeeDetailSerializers
from ..models.employee import Employees
from django.urls import reverse, reverse_lazy
from ..service.employee_service import EmployeeForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView


class EmployeeListView(generics.ListAPIView):
    """Class for displaying list of employees"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeDetailSerializers

    def get_queryset(self):
        """Function for filtering requested data"""
        queryset = Employees.objects.all()
        params = self.request.query_params
        date_from = params.get('date_from', None)
        date_to = params.get('date_to', None)
        department = params.get('department', None)
        if date_from:
            queryset = queryset.filter(date_of_birth__gte=date_from)
        if date_to:
            queryset = queryset.filter(date_of_birth__lte=date_to)
        if department:
            queryset = queryset.filter(depart__gte=department)
        return queryset


class EmployeeListView(ListView):
    """Class for dispalying models"""
    model = Employees
    template_name = 'employee_page.html'
    context_object_name = 'Employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Employees'] = Employees.objects.all()
        return context


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
