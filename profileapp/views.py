from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:wasdenn')
    template_name = 'profileapp/create.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

