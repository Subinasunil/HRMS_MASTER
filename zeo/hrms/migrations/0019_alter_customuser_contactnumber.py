# Generated by Django 5.0 on 2024-01-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0018_emp_documents_created_at_emp_documents_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ContactNumber',
            field=models.CharField(),
        ),
    ]