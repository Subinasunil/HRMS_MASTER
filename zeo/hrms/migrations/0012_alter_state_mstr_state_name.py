# Generated by Django 5.0 on 2023-12-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0011_rename_country_id_state_mstr_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state_mstr',
            name='state_name',
            field=models.CharField(max_length=50),
        ),
    ]
