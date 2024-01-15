from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView


@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('album:add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('author:profile')



@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('author:profile')
    pk_url_kwarg = 'id'