"""Contain information about urls of department_app application"""
from django.urls import path
from .views.employee_view import EmployeeListView
from .views.department_view import DepartmentListView


urlpatterns = [
    path('employee/', EmployeeListView.as_view()),
    path('department/', DepartmentListView.as_view())
]
