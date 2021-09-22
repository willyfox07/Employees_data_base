"""Module which contain form of department model"""
from ..models.department import Department
from django.forms import ModelForm


class DepartmentForm(ModelForm):
    """Class for creating form of department model"""
    class Meta:
        model = Department
        fields = '__all__'
