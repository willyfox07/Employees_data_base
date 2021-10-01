""" Module which contain serializer for employee model"""
from rest_framework import serializers
from department_app.models.employee import Employees


class EmployeeDetailSerializers(serializers.ModelSerializer):
    """Class for taking and transforming employee model data """
    department_name = serializers.StringRelatedField(source='depart', read_only=True)

    class Meta:
        """Class for installing settings of the main class"""
        model = Employees
        fields = '__all__'
