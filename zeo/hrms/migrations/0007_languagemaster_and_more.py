# Generated by Django 5.0 on 2023-12-22 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0006_alter_brnch_mstr_branch_nmbr_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='branch_mail',
            new_name='br_branch_mail',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='branch_nmbr_1',
            new_name='br_branch_nmbr_1',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='branch_nmbr_2',
            new_name='br_branch_nmbr_2',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='city',
            new_name='br_city',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='company_id',
            new_name='br_company_id',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='countries',
            new_name='br_countries',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='created_at',
            new_name='br_created_at',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='created_by',
            new_name='br_created_by',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='is_active',
            new_name='br_is_active',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='pincode',
            new_name='br_pincode',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='state_id',
            new_name='br_state_id',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='updated_at',
            new_name='br_updated_at',
        ),
        migrations.RenameField(
            model_name='brnch_mstr',
            old_name='updated_by',
            new_name='br_updated_by',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='ADMIN_UID',
            new_name='cmpny_ADMIN_UID',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='city',
            new_name='cmpny_city',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='countries',
            new_name='cmpny_countries',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='created_at',
            new_name='cmpny_created_at',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='created_by',
            new_name='cmpny_created_by',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='fax',
            new_name='cmpny_fax',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='gst',
            new_name='cmpny_gst',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='is_active',
            new_name='cmpny_is_active',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='logo',
            new_name='cmpny_logo',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='company_nmbr_1',
            new_name='cmpny_nmbr_1',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='Company_nmbr_2',
            new_name='cmpny_nmbr_2',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='pincode',
            new_name='cmpny_pincode',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='state_id',
            new_name='cmpny_state_id',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='updated_at',
            new_name='cmpny_updated_at',
        ),
        migrations.RenameField(
            model_name='cmpny_mastr',
            old_name='updated_by',
            new_name='cmpny_updated_by',
        ),
        migrations.RenameField(
            model_name='ctgry_master',
            old_name='description',
            new_name='ctgry_description',
        ),
        migrations.RenameField(
            model_name='emp_master',
            old_name='branch_id',
            new_name='emp_branch_id',
        ),
        migrations.RenameField(
            model_name='emp_master',
            old_name='company_id',
            new_name='emp_company_id',
        ),
        migrations.RenameField(
            model_name='emp_master',
            old_name='ctgry_id',
            new_name='emp_ctgry_id',
        ),
        migrations.RenameField(
            model_name='emp_master',
            old_name='dept_id',
            new_name='emp_dept_id',
        ),
        migrations.RenameField(
            model_name='emp_master',
            old_name='desgntn_id',
            new_name='emp_desgntn_id',
        ),
        migrations.CreateModel(
            name='EMP_dOCUMENTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_doc_name', models.CharField(max_length=50)),
                ('emp_doc_number', models.IntegerField()),
                ('emp_doc_issued_date', models.DateField()),
                ('emp_doc_expiry_date', models.DateField()),
                ('emp_doc_document', models.FileField(upload_to='')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.emp_master')),
            ],
        ),
        migrations.CreateModel(
            name='emp_family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ef_member_name', models.CharField(max_length=50)),
                ('emp_relation', models.CharField(max_length=50)),
                ('ef_company_expence', models.FloatField()),
                ('ef_date_of_birth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.emp_master')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpJobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_jh_from_date', models.DateField()),
                ('emp_jh_end_date', models.DateField()),
                ('emp_jh_company_name', models.CharField(max_length=50)),
                ('emp_jh_designation', models.CharField(verbose_name=50)),
                ('emp_jh_leaving_salary_permonth', models.FloatField()),
                ('emp_jh_reason', models.CharField(max_length=100)),
                ('emp_jh_years_experiance', models.FloatField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.emp_master')),
            ],
        ),
        migrations.CreateModel(
            name='EmpQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_qualification', models.CharField(max_length=50)),
                ('emp_qf_instituition', models.CharField(max_length=50)),
                ('emp_qf_year', models.DateField()),
                ('emp_qf_subject', models.CharField(max_length=50)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.emp_master')),
            ],
        ),
        migrations.AddField(
            model_name='emp_master',
            name='emp_languages',
            field=models.ManyToManyField(to='hrms.languagemaster'),
        ),
    ]