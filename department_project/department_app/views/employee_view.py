"""Module for control serializers of employee models"""
from rest_framework import viewsets, generics
from ..rest.employee_serializer import EmployeeDetailSerializers
from ..models.employee import Employees
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class EmployeeListView(viewsets.ViewSet):
    """Class for displaying list of employees"""

    def list(self, request):
        queryset = Employees.objects.all()
        serializer_class = EmployeeDetailSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Employees.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeDetailSerializers(user)
        return Response(serializer.data)

