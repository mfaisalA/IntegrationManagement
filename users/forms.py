from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import FacultyUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

class FacultyUserCreationForm(UserCreationForm):

    class Meta:
        model = FacultyUser
        fields = ('username', 'email', 'phone_number')

class FacultyUserChangeForm(UserChangeForm):

    class Meta:
        model = FacultyUser
        fields = ('username', 'email', 'phone_number')



# class FacultyMemberForm(forms.ModelForm):

#     class Meta:
#         model = FacultyMember
#         exclude = []
#         widgets= {
#             'password': forms.PasswordInput(),
#         }
