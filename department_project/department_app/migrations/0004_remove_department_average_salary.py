# Generated by Django 3.2.5 on 2021-09-13 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0003_auto_20210910_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='average_salary',
        ),
    ]
