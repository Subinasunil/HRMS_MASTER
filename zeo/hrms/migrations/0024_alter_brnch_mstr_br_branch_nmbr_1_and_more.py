# Generated by Django 5.0 on 2024-01-06 12:50

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0023_alter_brnch_mstr_br_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brnch_mstr',
            name='br_branch_nmbr_1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='brnch_mstr',
            name='br_branch_nmbr_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]