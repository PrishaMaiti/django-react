from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=20, default='', blank=False)
    last_name = models.CharField(max_length=20, default='', blank=False)
    gender = models.CharField(max_length=10, default='M', choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')])
    birthday = models.DateField(blank=False)
    address = models.CharField(max_length=100, default='', blank=False)
    phone_number = models.CharField(max_length=15, default='', blank=True)
    aff_school = models.CharField(max_length=30, default='', blank=False)
    class_level = models.CharField(max_length=5, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)