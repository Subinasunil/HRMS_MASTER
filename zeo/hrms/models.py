
# Create your models here.


from django.contrib.auth.models import User,Group
from django.db import models
#for customusertable
from django.contrib.auth.models import AbstractUser
#for phonenumber field
from phonenumber_field.modelfields import PhoneNumberField

#local import
from .manager import CustomUserManager

#USER MODELS
class CustomUser(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    CompanyRole = models.CharField(max_length=100,blank=True)
    ContactNumber = models.CharField()
    created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE,null=True, related_name='%(class)s_created_by' )
    companies = models.ManyToManyField('cmpny_mastr',blank=True)
    branches = models.ManyToManyField('brnch_mstr',blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

#COUNTRY MODELS
class cntry_mstr(models.Model):

    country_name = models.CharField(max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.country_name


#STATE MODEL
class state_mstr(models.Model):

    state_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey('cntry_mstr',on_delete=models.CASCADE)
    def __str__(self):
        return self.state_name

#CURRENCY MODEL
class crncy_mstr(models.Model):
    currency_name = models.CharField(max_length=50,unique=True)
    currency_code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=5, blank=True, null=True)
    # countries = models.ManyToManyField(cntry_mstr)  # Many-to-many relationship with Country model
    def __str__(self):
        return self.currency_name

#COMPANY MODEL
class cmpny_mastr(models.Model):

    cmpny_name = models.CharField(max_length=100,unique=True)
    cmpny_is_active = models.BooleanField(default=True)
    # country_id = models.ForeignKey('cntry_mstr',on_delete = models.CASCADE)
    cmpny_state_id = models.ForeignKey('state_mstr',on_delete=models.CASCADE)
    cmpny_city = models.CharField(max_length=50)
    cmpny_pincode = models.CharField(max_length=20)
    cmpny_nmbr_1 = PhoneNumberField(unique=True)
    cmpny_nmbr_2 = PhoneNumberField(blank=True)
    cmpny_mail = models.EmailField(unique=True)
    cmpny_logo = models.ImageField(upload_to='logos/')
    cmpny_fax =models.CharField(max_length=100,null=True,blank=True)
    cmpny_gst =models.CharField(max_length=100,null=True,blank=True)
    cmpny_country = models.ForeignKey('cntry_mstr',on_delete=models.SET_DEFAULT, default="1")  # Many-to-many relationship with Country model
    cmpny_created_at = models.DateTimeField(auto_now_add=True)
    cmpny_created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    cmpny_updated_at = models.DateTimeField(auto_now=True)
    cmpny_updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    # cmpny_ADMIN_UID = models.ForeignKey('CustomUser', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.cmpny_name
    
#branch model
class brnch_mstr(models.Model):
    branch_name = models.CharField(max_length=100)
    br_company_id = models.ForeignKey('cmpny_mastr',on_delete=models.CASCADE,null=True,blank=True)
    br_is_active = models.BooleanField(default=True)
    # country_id = models.ForeignKey('cntry_mstr',on_delete = models.CASCADE)
    br_state_id = models.ForeignKey('state_mstr',on_delete=models.SET_DEFAULT, default="1")
    br_city = models.CharField(max_length=50)
    br_pincode = models.CharField(max_length=20)
    br_branch_nmbr_1 = PhoneNumberField(unique=True)
    br_branch_nmbr_2 = PhoneNumberField(blank=True)
    br_branch_mail = models.EmailField(unique=True)
    br_country = models.ForeignKey('cntry_mstr',on_delete=models.SET_DEFAULT, default="1") 
    br_created_at = models.DateTimeField(auto_now_add=True)
    br_created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, related_name='%(class)s_created_by')
    br_updated_at = models.DateTimeField(auto_now=True)
    br_updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    def __str__(self):
        return self.branch_name
    

#departments model
class dept_master(models.Model):
    dept_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.dept_name

#designation master
class desgntn_master(models.Model):
    job_title =  models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.job_title

#CATOGARY master
class ctgry_master(models.Model):
    catogary_title =  models.CharField(max_length=50)
    ctgry_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.catogary_title

#LANGUAGE MASTER 
class LanguageMaster(models.Model):
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language


#employee master
class emp_master(models.Model):
    GENDER = {
        "M": "Male",
        "F": "Female",
        "O": "Other",
    }
    MARITAL_STATUS = {
        "M":"Married",
        "S":"Single",
        "D":"Other",
    }
    emp_first_name = models.CharField(max_length=50)
    emp_last_name = models.CharField(max_length=50)
    emp_gender = models.CharField(max_length=1,choices=GENDER)
    emp_date_of_birth = models.DateField()
    emp_personal_email =  models.EmailField(unique=True)
    emp_mobile_number_1 = PhoneNumberField(unique=True)
    emp_mobile_number_2 = PhoneNumberField(blank=True)
    emp_country_id = models.ForeignKey('cntry_mstr',on_delete = models.CASCADE)
    emp_state_id = models.ForeignKey('state_mstr',on_delete=models.CASCADE)
    emp_city = models.CharField(max_length=50)
    emp_permenent_address = models.CharField(max_length=200)
    emp_present_address = models.CharField(max_length=200,blank=True)
    emp_status =  models.BooleanField(default=True)
    emp_boss = models.ForeignKey('emp_master',on_delete = models.CASCADE)
    emp_hired_date = models.DateField(null=True)
    emp_active_date = models.DateField(null=True,blank=True)
    emp_relegion = models.CharField(max_length=50)
    emp_profile_pic = models.ImageField(upload_to='profile_pic/')
    emp_blood_group = models.CharField(max_length=50,blank=True)
    emp_nationality = models.CharField(blank=True)
    emp_marital_status = models.CharField(max_length=1,choices=MARITAL_STATUS)
    emp_father_name = models.CharField(max_length=50,blank=True)
    emp_mother_name = models.CharField(max_length=50,blank=True)
    emp_posting_location = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    is_active = models.BooleanField(default=True)
    is_ess = models.BooleanField(default=False)
    epm_ot_applicable = models.BooleanField(default=False)
    #foreign keys 
    emp_company_id = models.ForeignKey('cmpny_mastr',on_delete = models.CASCADE)
    emp_branch_id = models.ForeignKey('brnch_mstr',on_delete = models.CASCADE)
    emp_dept_id = models.ForeignKey('dept_master',on_delete = models.CASCADE)
    emp_desgntn_id = models.ForeignKey('desgntn_master',on_delete = models.CASCADE)
    emp_ctgry_id = models.ForeignKey('ctgry_master',on_delete = models.CASCADE)
    emp_languages = models.ManyToManyField(LanguageMaster)

#EMPLOYEE FAMILY(ef) data
class emp_family(models.Model):
    emp_id =models.ForeignKey('emp_master',on_delete = models.CASCADE)
    ef_member_name = models.CharField(max_length=50)
    emp_relation = models.CharField(max_length=50)
    ef_company_expence = models.FloatField()
    ef_date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
    is_active = models.BooleanField(default=True)

 
#EMPLOPYEE JOB HISTORY
class EmpJobHistory(models.Model):
    emp_id =models.ForeignKey('emp_master',on_delete = models.CASCADE)
    emp_jh_from_date = models.DateField()
    emp_jh_end_date = models.DateField()
    emp_jh_company_name=models.CharField(max_length=50)
    emp_jh_designation = models.CharField(50)
    emp_jh_leaving_salary_permonth = models.FloatField()
    emp_jh_reason = models.CharField(max_length=100)
    emp_jh_years_experiance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

#EMPLOYEE QUALIFICATION
class EmpQualification(models.Model):
    emp_id =models.ForeignKey('emp_master',on_delete = models.CASCADE)
    emp_qualification = models.CharField(max_length=50)
    emp_qf_instituition = models.CharField(max_length=50)
    emp_qf_year = models.DateField()
    emp_qf_subject= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')


#EMPLOYEE DOCUMENTS
class Emp_Documents(models.Model):
    emp_id =models.ForeignKey('emp_master',on_delete = models.CASCADE)
    emp_doc_name = models.CharField(max_length=50)
    emp_doc_number = models.IntegerField()
    emp_doc_issued_date = models.DateField()
    emp_doc_expiry_date = models.DateField()
    emp_doc_document = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')



class CustomUserGroup(models.Model):
    user = models.ManyToManyField(CustomUser,)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # Add any additional fields if needed