from django.contrib import admin

# Register your models here.
from .models import CustomUser,cmpny_mastr

admin.site.register(CustomUser)
admin.site.register(cmpny_mastr)