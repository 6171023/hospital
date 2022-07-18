import django.forms

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GeneralUser


class UserCreationForm(UserCreationForm):
    email = django.forms.EmailField(label=_("Email address"), required=True, help_text=_("Required."))

    password2 = django.forms.CharField(label='Confirm password', widget=django.forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise django.forms.ValidationError("Email is already used")
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

#form for user edit profile
class GeneralUserForm(django.forms.ModelForm):
    class Meta:
        model = GeneralUser
        exclude = ['user', 'uid']

#form for querying doctors
class DoctorQueryForm(django.forms.Form):

    male = django.forms.BooleanField(required=False)
    female = django.forms.BooleanField(required=False)
    other = django.forms.BooleanField(required=False)

    min_year = django.forms.IntegerField()