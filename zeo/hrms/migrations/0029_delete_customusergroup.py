# Generated by Django 5.0 on 2024-01-08 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0028_remove_cmpny_mastr_users_delete_customgroup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserGroup',
        ),
    ]