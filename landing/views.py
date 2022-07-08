from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('landing/index.html')
    context = {
        'status': "Working-In-Progress"
    }
    return HttpResponse(template.render(context, request))
    