from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, FacultyMemberForm
from .models import CustomUser, FacultyMember


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name']
    # inlines = [FacultyMemberAdminInline]


@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    add_form = FacultyMemberForm
    form = FacultyMemberForm
    model = FacultyMember
    list_display = ['getUsername', 'getName','phone_number',]


admin.site.register(CustomUser, CustomUserAdmin)