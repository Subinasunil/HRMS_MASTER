# Generated by Django 5.0.3 on 2024-03-28 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManagement', '0022_alter_customfield_unique_together_and_more'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='content_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='customfield',
            name='default_value',
            field=models.CharField(blank=True, help_text='You may leave blank. For Boolean use True or False', max_length=5000),
        ),
        migrations.AddField(
            model_name='customfield',
            name='field_choices',
            field=models.CharField(blank=True, help_text='List the choices you want displayed, separated by commas. This is only valid for Dropdown, Multiple, and Checkbox field types', max_length=2000),
        ),
        migrations.AddField(
            model_name='customfield',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customfield',
            name='mask',
            field=models.CharField(blank=True, help_text="You may leave blank. For user Jquery Mask, ex: '00/00/0000' for date.", max_length=5000),
        ),
        migrations.AddField(
            model_name='emp_master',
            name='custom_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_masters_customfield', to='EmpManagement.customfield'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='field_type',
            field=models.CharField(choices=[('t', 'Text'), ('a', 'Large Text Field'), ('i', 'Integer'), ('f', 'Floating point decimal'), ('b', 'Boolean (Yes/No)'), ('m', 'Dropdown Choices'), ('d', 'Date'), ('h', 'Date Time')], default='t', max_length=1),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterUniqueTogether(
            name='customfield',
            unique_together={('name', 'content_type')},
        ),
        migrations.DeleteModel(
            name='CustomFieldValue',
        ),
    ]
