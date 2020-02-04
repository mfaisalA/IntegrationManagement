from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import   FacultyUserCreationForm, FacultyUserChangeForm
from .models import  FacultyUser


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'first_name']
#     # inlines = [FacultyMemberAdminInline]


class FacultyUserAdmin(UserAdmin):
    add_form = FacultyUserCreationForm
    form = FacultyUserChangeForm
    model = FacultyUser
    fieldsets = [('Login Info',{'fields':['username', 'password']} ), ('Personal Info',{'fields':['first_name', 'email', 'phone_number', 'privileges']})]
    list_display = ['username', 'first_name','email', 'phone_number']


# @admin.register(FacultyMember)
# class FacultyMemberAdmin(admin.ModelAdmin):
#     add_form = FacultyMemberForm
#     form = FacultyMemberForm
#     model = FacultyMember
#     list_display = ['getUsername', 'getName','phone_number',]


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FacultyUser, FacultyUserAdmin)