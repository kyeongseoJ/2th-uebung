from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def wasdenn(request):
    if request.method=='POST':
           return render(request, 'accountapp/MOINMOIN.html',
                         context={'text':' POST METHOD!'})
    else:
           return render(request,'accountapp/MOINMOIN.html',
                         context={'text':' POST METHOD!'})
