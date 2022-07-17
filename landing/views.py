from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import UserCreationForm, GeneralUserForm
from .models import GeneralUser, Doctor
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

def get_doctor(request, uid):
    template = loader.get_template('landing/doctor_profile.html')
    if request.method == 'GET':
        doctor = Doctor.objects.get(uid=uid)
        context = {
            'name' : doctor.name,
            'gender' : doctor.get_gender_display(),
            'email' : doctor.user.email,
            'qualification' : doctor.qualification,
            'specialization' : doctor.specialization,
            'years_of_experience' : doctor.years_of_experience,
        }

    return HttpResponse(template.render(context, request))

def home_redir(request):
    return redirect('/home/')

def index(request):
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(None, request))