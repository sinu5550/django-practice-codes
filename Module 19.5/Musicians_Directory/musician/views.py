from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.



@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('musician:add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')