"""Module which contain serializer for department model """
from rest_framework import serializers
from ..models.department import Department
from ..models.employee import Employees


class DepartmentDetailSerializers(serializers.ModelSerializer):
    """Class for taking and transforming department model data """
    average_salary = serializers.SerializerMethodField('get_average')
    head_name = serializers.StringRelatedField(source='head', read_only=True)

    @staticmethod
    def get_average(obj):
        """Function for calculation average salary in every department"""
        department_employees = Employees.objects.filter(depart=obj.id)
        try:
            return round(sum([employee.salary for employee in department_employees])/len(department_employees), 2)
        except ZeroDivisionError:
            return 0

    class Meta:
        """Class for installing settings of the main class"""
        model = Department
        fields = '__all__'


