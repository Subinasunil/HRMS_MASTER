# Generated by Django 5.0 on 2024-01-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0031_customuser_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='branches',
            field=models.ManyToManyField(blank=True, to='hrms.brnch_mstr'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='companies',
            field=models.ManyToManyField(blank=True, to='hrms.cmpny_mastr'),
        ),
    ]