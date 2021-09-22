"""Contain information about urls of department_app application"""
from django.urls import path
from .views.employee_view import EmployeeListAPIView
from .views.department_view import DepartmentListAPIView


urlpatterns = [
    path('employee/', EmployeeListAPIView.as_view()),
    path('department/', DepartmentListAPIView.as_view())
]

