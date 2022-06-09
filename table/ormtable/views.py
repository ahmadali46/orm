from importlib.resources import contents
from unicodedata import name
from django.shortcuts import render
from matplotlib.pyplot import cla
from requests import request
from django.shortcuts import render,redirect
from django.db import models
from .models import *
from . forms import *
def index(request):
    form=student.objects.raw('select studid,first_name from employeetable group by first_name having count(first_name)>2')
    # form  = student.objects.all()
    curs=course.objects.all()
    content = {
    'form':form,'curs':curs
    }
    return render(request,'index.html',content)
    
# Create your views here.
