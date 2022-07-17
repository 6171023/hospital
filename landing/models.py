from django.db import models
from django.contrib.auth.models import User
#prefix uid with the type of user

class GeneralUser(models.Model):
    #TODO: regex validation for dob and tel 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    uid = models.PositiveIntegerField()

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
    uid = models.PositiveIntegerField()

    GENDER_CHOICES = [(0, 'Male'),(1, 'Female'),(2, 'Other'), (3, 'Do not wish to answer')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    qualification = models.TextField(max_length=512)
    specialization = models.TextField(max_length=512)
    years_of_experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name 
