from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import UserCreationForm, GeneralUserForm
from .models import GeneralUser
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def save_profile(request):
    #TODO, random/assign UID
    if request.method == 'POST':
        profile = GeneralUser.objects.get(user=request.user)
        form = GeneralUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        profile = GeneralUser.objects.get(user=request.user)
        form = GeneralUserForm(instance=profile)

    return render(request, 'landing/profile.html', {'form': form})

def home_redir(request):
    return redirect('/home/')

def index(request):
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(None, request))