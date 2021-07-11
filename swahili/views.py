from django.shortcuts import render
from .models import *

# Create your views here.
def homeView(request):
    return render(request, 'home.html')
