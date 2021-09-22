"""This module contain models for department"""

from django.db import models


class Department(models.Model):
    """Model contain info about department """
    name = models.CharField("name of department",
                            max_length=50)
    number_of_employees = models.IntegerField()
    head = models.ForeignKey('Employees', on_delete=models.CASCADE,blank = True, null=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
