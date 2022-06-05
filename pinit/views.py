from django.shortcuts import render,redirect
from .models import Profiles,Comment,Images
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def home(request):
    images =Images.get_all_images()
    return render(request, 'home.html', {'images':images})