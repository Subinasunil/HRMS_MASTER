# Generated by Django 5.0 on 2024-01-08 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0027_cmpny_mastr_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmpny_mastr',
            name='users',
        ),
        migrations.DeleteModel(
            name='CustomGroup',
        ),
    ]