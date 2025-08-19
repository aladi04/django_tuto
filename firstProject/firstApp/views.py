from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour

def index(request):
    return render(request, 'django_app/index.html')
