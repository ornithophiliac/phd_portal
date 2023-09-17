from django.shortcuts import render
from django.http import HttpResponse

from homepage.models import RegistrationDetail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Ensure this import is present
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    registration_details = RegistrationDetail.objects.all()
    return render(request, 'homepage/index.html', {'registration_details': registration_details})

def about(request):
    return render(request,"homepage/about.html")

# def register(request):
#     return render(request,"homepage/register.html")

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Replace 'home' with your desired redirection URL after login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Replace 'home' with your desired redirection URL after signup
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request, 'homepage/login.html')

def about_us(request):
    video_url = 'images/Untitled design.mp4'
    return render(request, 'about.html', {'images/Untitled design.mp4': video_url})