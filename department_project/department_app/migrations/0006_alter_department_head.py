# Generated by Django 3.2.5 on 2021-09-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0005_alter_department_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(default='Software', null=True, on_delete=django.db.models.deletion.CASCADE, to='department_app.employees'),
        ),
    ]
