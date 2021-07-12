from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import MoinMoin

def wasdenn(request):
    if request.method=='POST':

        temp = request.POST.get('moinmoin_input')

        new_moinmoin = MoinMoin()
        new_moinmoin.text = temp
        new_moinmoin.save()

        return HttpResponseRedirect(reverse('accountapp:wasdenn'))

    else:
           MoinMoin_list = MoinMoin.objects.all()
           return render(request,'accountapp/MOINMOIN.html',
                         context={'MoinMoin_list': MoinMoin_list})