from django.shortcuts import loader
from django.http import HttpResponse
from .models import positions


def careers(request):
    template = loader.get_template('careers_home.html')
    return HttpResponse(template.render())

def careersdata(request):
    cdata = positions.objects.all().values()
    template = loader.get_template('careersdata.html')
    context = {
        'cdata': cdata,
    }
    return HttpResponse(template.render(context,request))

