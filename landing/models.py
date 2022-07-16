from django.db import models

class Allergy(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name 

class GeneralUser(models.Model):
    #TODO: regex validation for dob and tel 
    name = models.CharField(max_length=256)

    GENDER_CHOICES = [(0, 'Male'),(1, 'Female'),(2, 'Other'), (3, 'Do not wish to answer')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    dob = models.DateField()
    allergies = models.ManyToManyField(Allergy)
    address = models.TextField(max_length=512)
    tel = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return self.name 

#TODO: Make Doctor class with following values:
#years_of_experience, qualification, specialization, gender, email