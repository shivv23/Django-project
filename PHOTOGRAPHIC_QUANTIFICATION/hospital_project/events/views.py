from django.shortcuts import loader
from django.http import HttpResponse
from .models import events


def event1(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def eventdata(request):
    edata = events.objects.all().values()
    template = loader.get_template('eventsdata.html')
    context = {
        'edata': edata,
    }
    return HttpResponse(template.render(context, request))