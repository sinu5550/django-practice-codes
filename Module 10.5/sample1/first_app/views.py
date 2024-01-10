from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d= {'author': 'Rahim','age':20,'lst':['python','is','best'],'today':datetime.datetime.now(), 'lst2' : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
    ],}

    return render(request,'first_app/home.html',d)