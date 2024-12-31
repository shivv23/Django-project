from django.shortcuts import loader
from django.http import HttpResponse

def doctors(request):
    template = loader.get_template('doctorshome.html')
    return HttpResponse(template.render())

