# Generated by Django 5.0 on 2024-01-08 08:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0026_alter_brnch_mstr_br_branch_mail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmpny_mastr',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]