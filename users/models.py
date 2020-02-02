from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    pass


class FacultyMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+3xxxxxxx'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    PRIV_LECTURER = 'lec'
    PRIV_COURSE_HEAD = 'crs'
    PRIV_CHOICES = [(PRIV_LECTURER,'Lecurer'), (PRIV_COURSE_HEAD, 'Course Head')]
    privileges = MultiSelectField(choices=PRIV_CHOICES, max_length=3)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    