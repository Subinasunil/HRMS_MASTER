# Generated by Django 5.0 on 2024-01-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0024_alter_brnch_mstr_br_branch_nmbr_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brnch_mstr',
            name='br_branch_mail',
            field=models.EmailField(max_length=254),
        ),
    ]
