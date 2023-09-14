from django.shortcuts import render
from django.http import HttpResponse

from homepage.models import RegistrationDetail

# Create your views here.

def home(request):
    registration_details = RegistrationDetail.objects.all()
    return render(request, 'homepage/index.html', {'registration_details': registration_details})

def about(request):
    return render(request,"homepage/about.html")

def register(request):
    return render(request,"homepage/register.html")