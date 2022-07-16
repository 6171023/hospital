from django.contrib import admin
from .models import GeneralUser, Doctor
# Register your models here.
admin.site.register(GeneralUser)
admin.site.register(Doctor)