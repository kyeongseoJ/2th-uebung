from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def wasdenn (request):
    return render(request, 'accountapp/MOINMOIN.html')