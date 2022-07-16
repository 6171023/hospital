import django.forms

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    email = django.forms.EmailField(label=_("Email address"), required=True, help_text=_("Required."))

    password2 = django.forms.CharField(label='Confirm password', widget=django.forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

#TODO form for user edit profile