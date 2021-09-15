"""Module which contain serializer for department model """
from rest_framework import serializers
from ..models.department import Department


class DepartmentDetailSerializers(serializers.ModelSerializer):
    """Class for taking and transforming department model data """
    class Meta:
        """Class for installing settings of the main class"""
        model = Department
        fields = '__all__'
