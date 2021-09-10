from django.contrib import admin
from .models import Department
from .models import Employees

admin.site.register(Department)
admin.site.register(Employees)
