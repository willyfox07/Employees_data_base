"""Contain information about urls of department_app application"""
from django.urls import path
from .views.employee_view import EmployeeListAPIView
from .views.department_view import DepartmentListAPIView

app_name = 'department_app'
urlpatterns = [
    path(r'employee/', EmployeeListAPIView.as_view(), name="employee_api"),
    path(r'department/', DepartmentListAPIView.as_view(), name="department_api")
]

