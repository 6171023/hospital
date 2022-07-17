from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import GeneralUser, Doctor

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class GeneralUserInline(admin.StackedInline):
    model = GeneralUser
    can_delete = False
    verbose_name_plural = 'general users'

class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    verbose_name_plural = 'doctors'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (GeneralUserInline, DoctorInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)