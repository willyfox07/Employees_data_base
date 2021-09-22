"""Module which contain form of department model"""
from ..models.employee import Employees
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    """Class for creating form of employee model"""
    class Meta:
        model = Employees
        fields = '__all__'