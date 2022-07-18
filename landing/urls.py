from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_redir, name='redir'),
    path('home/', views.home, name='home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),  
    path('accounts/profile/', views.save_profile, name='profile'),
    path('doctor/<int:uid>', views.get_doctor, name='get_doctor'),  
    path('view/doctors/', views.doctor_view, name='doctor_view'),
]