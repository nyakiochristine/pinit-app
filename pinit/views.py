from django.shortcuts import render,redirect
from .models import Profiles,Comment,Images
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def home(request):
    images =Images.get_all_images()
    return render(request, 'home.html', {'images':images})

def  search(request):
    if 'search' in request.GET  and request.GET['search']:
        search_term = request.GET.get['search']
        profiles = Profiles.get_profile_by_name(search_term)
        message = f'{search_term}'
        return render(request, {'profiles':profiles},{'search_term':search_term})
    else:
        message = 'Search Username'
        return render(request, 'search.html', {'message':message})