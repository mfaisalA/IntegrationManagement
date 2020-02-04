from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

# class CustomUser(AbstractUser):
#     pass


class FacultyUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+3xxxxxxx'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    PRIV_LECTURER = 'lec'
    PRIV_COURSE_HEAD = 'crs'
    PRIV_CHOICES = [(PRIV_LECTURER,'Lecurer'), (PRIV_COURSE_HEAD, 'Course Head')]
    privileges = MultiSelectField(choices=PRIV_CHOICES, max_length=3)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Faculty User'
        verbose_name_plural = 'Faculty Users'


# class FacultyMember(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
#     # first_name = models.CharField(max_length=100)
#     # last_name = models.CharField(max_length=100)
#     # email = models.EmailField(max_length=100)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+3xxxxxxx'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

#     PRIV_LECTURER = 'lec'
#     PRIV_COURSE_HEAD = 'crs'
#     PRIV_CHOICES = [(PRIV_LECTURER,'Lecurer'), (PRIV_COURSE_HEAD, 'Course Head')]
#     privileges = MultiSelectField(choices=PRIV_CHOICES, max_length=3)
#     # username = models.CharField(max_length=50, unique=True)
#     # password = models.CharField(max_length=50)

#     def getUsername(self):
#         return self.user.username
#     getUsername.short_description = 'Username'

#     def getName(self):
#         return self.user.first_name
#     getName.short_description = 'First Name'
    
#     def __str__(self):
#         return self.user.username
