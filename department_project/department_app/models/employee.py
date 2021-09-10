"""This module contain information about employee"""
from django.db import models


class Employees(models.Model):
    """Model contain info about employees"""
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    position_held = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    depart = models.ForeignKey('Department', on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.surname} {self.name}'


    class Meta:
        """Class for model configuration"""
        ordering = ['name']
        verbose_name = 'Information about employee'
