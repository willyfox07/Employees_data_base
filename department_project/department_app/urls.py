"""Contain information about urls of department_app application"""
from django.urls import path, include
from .views.employee_view import EmployeeListView
from .views.department_view import DepartmentListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'employee', EmployeeListView, basename='employee_list')
router.register(r'department', DepartmentListView, basename='department_list')
router.register(r'department/<int:pk>/', DepartmentListView, basename='department_detail')
router.register(r'employee/<int:pk>/', EmployeeListView, basename='employee_detail')

urlpatterns = [
    path(' ', include(router.urls))
]
