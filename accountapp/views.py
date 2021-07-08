from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import MoinMoin

def wasdenn(request):
    if request.method=='POST':

        temp = request.POST.get('MoinMoin_input')

        new_moinmoin = MoinMoin()
        new_moinmoin.text = temp
        new_moinmoin.save()

           return render(request, 'accountapp/MOINMOIN.html',
                         context={'moinmoin_output':new_moinmoin})
    else:
           return render(request,'accountapp/MOINMOIN.html',
                         context={'text':' POST METHOD!'})