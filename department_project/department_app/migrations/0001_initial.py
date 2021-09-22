"""Module for creating migrations"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Class wich contain all migrations"""
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of department')),
                ('number_of_employees', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('position_held', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             to='department_app.department')),
            ],
            options={
                'verbose_name': 'Information about employee',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='department_app.employees'),
        ),
    ]
