from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics,viewsets,permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.generics import ListAPIView
# from .permissions import 
from django.contrib.auth.models import User,Group,Permission
#jwt token
from . permissions import IsSuperAdminUser,IsSelfOrSuperAdmin
# Create your views here.

from rest_framework import viewsets
from .models import CustomUser,cmpny_mastr,cntry_mstr,state_mstr,brnch_mstr,dept_master,desgntn_master,ctgry_master,crncy_mstr,emp_master,emp_family,LanguageMaster,EmpJobHistory,EmpQualification,Emp_Documents,CustomUserGroup
from .serializers import (CustomUserSerializer,CompanySerializer,
                          CountrySerializer,StateSerializer,BranchSerializer,
                          DeptSerializer,CtgrySerializer,DesgSerializer,CurrencySerializer
                          ,EmpSerializer,EmpFamSerializer,Emp_qf_Serializer,
                          LanguageMaster,LanguageMasterSerializer,EmpJobHistorySerializer,
                          DocumentSerializer,RoleSerializer,PermissionSerializer,CustomUserGroupSerializer)

#permissions
from . permissions import IsAdminUser,IsSuperUser



class RegisterUserAPIView(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsSelfOrSuperAdmin]
        else:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
   

class UserListView(ListAPIView):
    def get_serializer_class(self):
        # Add logic to determine which serializer to use based on the request or other conditions
        return CustomUserSerializer  # Return your serializer class
    queryset = CustomUser.objects.all()
    serializer = CustomUserSerializer
    permission_classes = (IsSuperUser )



class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

#COMPNY 
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = cmpny_mastr.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,] 
    def perform_create(self, serializer):
        company_instance = serializer.save()  # Save the parent instance
        branch_exists = brnch_mstr.objects.filter(br_company_id=company_instance).exists()
        if not branch_exists:
            replicated_data = {

                # Replicate necessary fields from the parent to create a child record
                # For example, replicate 'name' from ParentModel to 'child_name' in ChildModel
                'branch_name': company_instance.cmpny_name,  # Replace with your field names
                'br_state_id':company_instance.cmpny_state_id,
                'br_country':company_instance.cmpny_country,
                'br_city':company_instance.cmpny_city,
                'br_company_id':company_instance,
                'br_created_by':company_instance.cmpny_created_by,
                'br_updated_by':company_instance.cmpny_updated_by,
                'br_branch_mail':company_instance.cmpny_mail,
                'br_branch_nmbr_1':company_instance.cmpny_nmbr_1,
                # Add other fields as needed

            }
            brnch_mstr.objects.create(**replicated_data)

        return Response(serializer.data, status=201)
#BRANCH 
class BranchViewSet(viewsets.ModelViewSet):
    queryset = brnch_mstr.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,] 
    # def create_branch(sender, instance, created, **kwargs):
    #     if created:
    #         brnch_mstr.objects.create(company=instance, branch_name=f"{instance.id} Branch")
     
#DEPARTMENT 
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = dept_master.objects.all()
    serializer_class = DeptSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [AllowAny,] 
    
#DESIGNATION 
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = desgntn_master.objects.all()
    serializer_class = DesgSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,] 
    
#CATOGARY CRUD
class CatogoryViewSet(viewsets.ModelViewSet):
    queryset = ctgry_master.objects.all()
    serializer_class = CtgrySerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsSuperUser,] 
    


#COUNTRY CRUD
class CountryViewSet(viewsets.ModelViewSet):
    queryset = cntry_mstr.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsSuperUser,] 
    

#STATE CRUD
class StateViewSet(viewsets.ModelViewSet):
    queryset = state_mstr.objects.all()
    serializer_class = StateSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsSuperUser,] 
    

#CURRENCY CRUD+
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = crncy_mstr.objects.all()
    serializer_class = CurrencySerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsSuperUser,] 
    
#EMPLOYEE CRUD
class EmpViewSet(viewsets.ModelViewSet):
    queryset = emp_master.objects.all()
    serializer_class = EmpSerializer
    permission_classes = [IsSuperUser]

#EMP_FAMILY
class EmpFamViewSet(viewsets.ModelViewSet):
    queryset = emp_family.objects.all()
    serializer_class = EmpFamSerializer
    permission_classes = [IsSuperUser]
#EMP_LANGUAGE
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = LanguageMaster.objects.all()
    serializer_class = LanguageMasterSerializer
    permission_classes = [IsSuperUser]
#EMP_JOB HISTORY
class EmpJobHistoryvSet(viewsets.ModelViewSet):
    queryset = EmpJobHistory.objects.all()
    serializer_class = EmpJobHistorySerializer
    permission_classes = [IsSuperUser]
#EMP_QUALIFICATION HISTORY
class Emp_QualificationViewSet(viewsets.ModelViewSet):
    queryset = EmpQualification.objects.all()
    serializer_class = Emp_qf_Serializer
    permission_classes = [IsSuperUser]

#EMP_DOCUMENT HISTORY
class Emp_DocumentViewSet(viewsets.ModelViewSet):
    queryset = Emp_Documents.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsSuperUser]

#usergroups or roles
class UserRolesViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsSuperUser]

# user grouping with permissions

class UserandPermissionGrouping(viewsets.ModelViewSet):
    queryset = CustomUserGroup.objects.all()
    serializer_class = CustomUserGroupSerializer
    permission_classes = [IsSuperUser]