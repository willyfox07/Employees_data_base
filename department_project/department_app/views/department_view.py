"""Module for control serializers of department models"""
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from ..rest.department_serializer import DepartmentDetailSerializers
from ..models.department import Department
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class DepartmentListView(viewsets.ViewSet):
    """Class for displaying list of departments"""

    def list(self, request):
        queryset = Department.objects.all()
        serializer_class = DepartmentDetailSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentDetailSerializers(user)
        return Response(serializer.data)


