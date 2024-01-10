from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (RegisterUserAPIView,CompanyViewSet,CountryViewSet,StateViewSet,BranchViewSet,
                    DepartmentViewSet,DesignationViewSet,CatogoryViewSet,CurrencyViewSet,EmpViewSet,
                    EmpFamViewSet,LanguageViewSet,Emp_DocumentViewSet,EmpJobHistoryvSet,Emp_QualificationViewSet,
                    UserListView,UserRolesViewSet,PermissionViewSet,UserandPermissionGrouping)

router = DefaultRouter()

router.register(r'user', RegisterUserAPIView)
router.register(r'Company', CompanyViewSet)
router.register(r'Country', CountryViewSet)
router.register(r'State', StateViewSet)
router.register(r'Branch', BranchViewSet)
router.register(r'Department', DepartmentViewSet)
router.register(r'Designation', DesignationViewSet)
router.register(r'Catogory', CatogoryViewSet)
router.register(r'Currency', CurrencyViewSet)
router.register(r'Employee', EmpViewSet)
router.register(r'emp-Family', EmpFamViewSet)
router.register(r'emp-Language', LanguageViewSet)
router.register(r'emp-JobHistory', EmpJobHistoryvSet)
router.register(r'emp-Qualification', Emp_QualificationViewSet)
router.register(r'emp-Documents', Emp_DocumentViewSet)
router.register(r'Role-Grouping', UserRolesViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'UserandPermissionGrouping', UserandPermissionGrouping)






urlpatterns = [
    # Other paths
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/userregister/',RegisterUserAPIView.as_view(),),
    path('api/userlist/', UserListView.as_view(), ),

]