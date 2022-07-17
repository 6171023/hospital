from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_redir, name='redir'),
    path('home/', views.index, name='index'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),  
    path('accounts/profile/', views.save_profile, name='profile'),  
]