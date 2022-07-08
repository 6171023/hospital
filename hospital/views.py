from django.shortcuts import redirect

def home_redir(request):
    return redirect('/home/')