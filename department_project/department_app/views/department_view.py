"""Module for control serializers of department models"""
from rest_framework import generics
from ..rest.department_serializer import DepartmentDetailSerializers
from ..models.department import Department


class DepartmentListAPIView(generics.ListAPIView):
    """Class for displaying list of departments"""
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializers

    def get_queryset(self):
        """Function for filtering requested data"""
        queryset = Department.objects.all()
        params = self.request.query_params
        min = params.get('min', None)
        max = params.get('max', None)
        location = params.get('location', None)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if min:
            queryset = queryset.filter(number_of_employees__gte=min)
        if max:
            queryset = queryset.filter(number_of_employees__lte=max)
        return queryset



