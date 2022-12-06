from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from .models import CustomUser, Criteria

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)

class CriteriaAdmin(admin.ModelAdmin):
    model = Criteria
admin.site.register(Criteria, CriteriaAdmin)
