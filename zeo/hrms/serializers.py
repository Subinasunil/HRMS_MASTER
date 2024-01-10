from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser,cmpny_mastr,cntry_mstr,state_mstr,brnch_mstr,dept_master,desgntn_master,ctgry_master,crncy_mstr,emp_master,emp_family,LanguageMaster,EmpJobHistory,Emp_Documents,EmpQualification,CustomUserGroup
from django.contrib.auth.models import User,Group,Permission

#USER CREDENTIALS


class UserSerializer(serializers.ModelSerializer):
    # making created_by field to current user
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault(), required=False)
    class Meta:
        model = CustomUser
        fields =('id','username','first_name','last_name','is_staff','email','CompanyRole','ContactNumber','password','created_by','companies','branches')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        # function for authenticated users automatically save created_by field and untuhentictaed user created_by field will save null value
        created_by = self.context['request'].user if self.context['request'].user.is_authenticated else None
        validated_data['created_by'] = created_by



        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user
#user list
class CustomUserSerializer(UserSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Check if the user is authenticated
        user = self.context['request'].user
        is_authenticated = user.is_authenticated
        
        # Hide 'companies' field if the user is not authenticated
        if not is_authenticated:
            self.fields.pop('companies')
            self.fields.pop('branches')
 
#COMPANY CREDENTIALS
class CompanySerializer(serializers.ModelSerializer):
    cmpny_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cmpny_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = cmpny_mastr
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    br_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    br_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = brnch_mstr
        fields = '__all__'


#DEPARTMENT CREDENTIALS
class DeptSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = dept_master
        fields= '__all__'

#DESIGNATION CREDENTIALS
class DesgSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = desgntn_master
        fields= '__all__'

#CATOGARY CREDENTIALS
class CtgrySerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ctgry_master
        fields= '__all__'



#COUNTRY CREDENTIALS
class CountrySerializer(serializers.ModelSerializer):
    # br_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # br_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = cntry_mstr
        fields = '__all__'


#STATE CREDENTIALS
class StateSerializer(serializers.ModelSerializer):
    # br_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # br_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # country_name = serializers.CharField(source='country.country_name',write_only=True)
    class Meta:
        model = state_mstr
        fields = '__all__'
    # def create(self, validated_data):
    #     country_name = validated_data.pop('country_name')  # Extract country name
    #     country_name, created = cntry_mstr.objects.get(name=country_name)  # Get the Country object by name
    #     state = state_mstr.objects.create(country_name=country_name, **validated_data)
    #     return state

#CURRENCY CREDENTIALS
class CurrencySerializer(serializers.ModelSerializer):
    # br_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # br_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = crncy_mstr
        fields = '__all__'

#EMPLOYEE CREDENTIALS
class EmpSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = emp_master
        fields = '__all__'
        # extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

#EMPLOYEE FAMILY
class EmpFamSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model= emp_family
        fields = '__all__'

#LANGUAGES
class LanguageMasterSerializer(serializers.ModelSerializer):
    # br_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # br_updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model= LanguageMaster
        fields = '__all__'
#experiance
class EmpJobHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model= EmpJobHistory
        fields = '__all__'

#EMPLOYEE QUALIFICATION CREDENTIALS
class Emp_qf_Serializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = EmpQualification
        fields= '__all__'


#EMPLOYEE DOCUMENT CREDENTIALS
class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Emp_Documents
        fields= '__all__'


#user group creation
class RoleSerializer(serializers.ModelSerializer):
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Group
        fields='__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class CustomUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserGroup
        fields = '__all__'