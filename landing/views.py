from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import UserCreationForm, GeneralUserForm, DoctorQueryForm
from .models import GeneralUser, Doctor
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def save_profile(request):
    if not request.user.is_authenticated:
        return redirect('/home/')

    try:
        profile = GeneralUser.objects.get(user=request.user)
    except GeneralUser.DoesNotExist:
        profile = GeneralUser(user=request.user)

    if request.method == 'POST':
        form = GeneralUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = GeneralUserForm(instance=profile)

    return render(request, 'landing/profile.html', {'form': form})

def get_doctor(request, uid):
    if not request.user.is_authenticated:
        return redirect('/home/')

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

def doctor_view(request):
    if not request.user.is_authenticated:
        return redirect('/home/')
    
    if request.method == 'POST':
        form = DoctorQueryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = DoctorQueryForm()

    return render(request, 'landing/doctor_view.html', {'form': form})

def home_redir(request):
    return redirect('/home/')

def home(request):
    if request.user.is_authenticated:
        template = loader.get_template('landing/home.html')

        is_doctor = False

        #check first if the user is a doctor, if not then they are a general user
        user = Doctor.objects.filter(user=request.user)

        if len(user) == 1:
            is_doctor = True
        else:
            try:
                user = GeneralUser.objects.get(user=request.user)
            except GeneralUser.DoesNotExist:
                return redirect('/accounts/profile/')

        context = {
            'user' : user,
            'is_doctor' : is_doctor,
        }
    else:
        template = loader.get_template('landing/index.html')
        context = None
    return HttpResponse(template.render(context, request))