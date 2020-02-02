from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, FacultyMember

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class FacultyMemberForm(forms.ModelForm):

    class Meta:
        model = FacultyMember
        exclude = []
        widgets= {
            'password': forms.PasswordInput(),
        }
