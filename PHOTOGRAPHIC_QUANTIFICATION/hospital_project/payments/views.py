from django.shortcuts import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import payments


def paymentss(request):
    template = loader.get_template('payments.html')
    return HttpResponse(template.render())

def paymentsdata(request):
    pdata = payments.objects.all().values()
    template = loader.get_template('paymentsdata.html')
    context = {
        'pdata': pdata,
    }
    return HttpResponse(template.render(context,request))

def paymentsdata(request):
    template = loader.get_template('paymentsdatawrite.html')
    return HttpResponse(template.render())

@csrf_exempt
def paymentsdatawrite(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Remarks = request.POST.get("Remarks")
        contact = request.POST.get('contact')
        emailID = request.POST.get('emailID')
        consultationFee = request.POST.get('consultationFee')

        temp = payments(
            Name=Name,
            Remarks=Remarks,
            contact=contact,
            emailID=emailID,
            consultationFee=consultationFee,
            )
        temp.save()
        return redirect("/")
    else:
        return HttpResponse("Invalid request method..")
