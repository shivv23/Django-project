from django.shortcuts import loader
from django.http import HttpResponse

def careers(request):
    template = loader.get_template('careers_home.html')
    return HttpResponse(template.render())

