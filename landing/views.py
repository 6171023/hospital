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
    #TODO, assign unique UID
    profile = GeneralUser.objects.get(user=request.user)

    if request.method == 'POST':
        form = GeneralUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
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

def home(request):
    if request.user.is_authenticated:
        template = loader.get_template('landing/home.html')

        is_doctor = False

        #check first if the user is a doctor, if not then they are a general user
        try:
            user = Doctor.objects.get(user=request.user)
            is_doctor = True
        except Doctor.DoesNotExist:
            user = GeneralUser.objects.get(user=request.user)

        context = {
            'user' : user,
            'is_doctor' : is_doctor,
        }
    else:
        template = loader.get_template('landing/index.html')
        context = None
    return HttpResponse(template.render(context, request))