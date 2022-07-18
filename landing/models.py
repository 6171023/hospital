from django.db import models
from django.contrib.auth.models import User
#uid will be prefixed with the type of user: 1 is GeneralUser and 2 is Doctor

class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    uid = models.AutoField(primary_key=True)

    GENDER_CHOICES = [(0, 'Male'),(1, 'Female'),(2, 'Other'), (3, 'Do not wish to answer')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    dob = models.DateField()
    allergies = models.CharField(max_length=64)
    address = models.TextField(max_length=512)
    tel = models.CharField(max_length=16)

    def __str__(self):
        return self.name 

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    uid = models.AutoField(primary_key=True)

    GENDER_CHOICES = [(0, 'Male'),(1, 'Female'),(2, 'Other'), (3, 'Do not wish to answer')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    qualification = models.TextField(max_length=512)
    specialization = models.TextField(max_length=512)
    years_of_experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name 

class Reserving(models.Model):
    guser = models.OneToOneField(User)
    doctor = models.OneToOneField(User)
    date = models.DateField()

    def __str__(self):
        return self.name 
