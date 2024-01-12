from django.shortcuts import render
from album.models import Album
# Create your views here.

def home(request):
    a_data = Album.objects.all()
    return render(request,'home.html',{'a_data': a_data})