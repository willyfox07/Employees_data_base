""" Module which contain serializer for employee model"""
from rest_framework import serializers
from ..models.employee import Employees


class EmployeeDetailSerializers(serializers.ModelSerializer):
    """Class for taking and transforming employee model data """
    class Meta:
        """Class for installing settings of the main class"""
        model = Employees
        fields = '__all__'
