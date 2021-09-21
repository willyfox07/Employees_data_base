"""department_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from department_app.views.department_view import DepartmentCreateView, DepartmentDeleteView,\
                                                  DepartmentUpdateView, DepartmentListView
from department_app.views.employee_view import EmployeeCreateView, EmployeeDeleteView,\
                                                  EmployeeUpdateView, EmployeeListView

urlpatterns = [
    path('', DepartmentListView.as_view(), name="department_page"),
    path('admin/', admin.site.urls),
    path('api/v1/', include('department_app.urls')),
    path('create_department/', DepartmentCreateView.as_view(), name="create_department"),
    path('edit_department/<int:pk>', DepartmentUpdateView.as_view(), name="edit_department"),
    path('delete_department/<int:pk>', DepartmentDeleteView.as_view(), name="delete_department"),
    path('employee/',EmployeeListView.as_view(), name="employee_page"),
    path('employee/create_employee/', EmployeeCreateView.as_view(), name="create_employee"),
    path('employee/edit_employee/<int:pk>', EmployeeUpdateView.as_view(), name="edit_employee"),
    path('employee/delete_employee/<int:pk>', EmployeeDeleteView.as_view(), name="delete_employee"),


]