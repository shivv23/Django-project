from django.shortcuts import loader
from django.http import HttpResponse
from .models import doctorinfo

def doctors(request):
    template = loader.get_template('doctorshome.html')
    return HttpResponse(template.render())

def doctorsdata(request):
    ddata = doctorinfo.objects.all().values()
    template = loader.get_template('doctorsdata.html')
    context = {
        'ddata': ddata,
    }
    return HttpResponse(template.render(context,request))

