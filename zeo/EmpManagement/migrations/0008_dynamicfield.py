# Generated by Django 5.0.3 on 2024-03-27 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManagement', '0007_alter_emp_master_emp_marital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('field_value', models.CharField(max_length=100)),
                ('emp_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpManagement.emp_master')),
            ],
        ),
    ]