"""Module for control serializers of department models"""
from rest_framework import generics
from ..rest.department_serializer import DepartmentDetailSerializers
from ..models.department import Department
from django.shortcuts import render, redirect
from ..service.department_service import DepartmentForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView,\
                                    ListView, DeleteView


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


class DepartmentListView(ListView):
    """Class for dispalying models"""
    #model = Department
    template_name = 'department_page.html'
    #context_object_name = 'Department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Department'] = Department.objects.all()
        return context

    def get_queryset(self):
        queryset = Department.objects.all()
        params = self.request.GET
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


class DepartmentDeleteView(DeleteView):
    """Class for deleting model"""
    model = Department
    success_url = reverse_lazy('department_page')


