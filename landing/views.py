from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic




# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home_redir(request):
    return redirect('/home/')

def index(request):
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(None, request))