"""Module for control serializers of employee models"""
from rest_framework import generics
from department_app.rest.employee_serializer import EmployeeDetailSerializers
from department_app.models.employee import Employees


class EmployeeListAPIView(generics.ListAPIView):
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
            queryset = queryset.filter(depart__name=department)
        return queryset






