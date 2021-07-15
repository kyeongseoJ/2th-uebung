from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

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

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:wasdenn')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url =reverse_lazy('accountapp:wasdenn')
    template_name = 'accountapp/update.html'