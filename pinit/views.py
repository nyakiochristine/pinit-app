from django.shortcuts import render,redirect
from .models import Profiles,Comment,Images
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PostCommentForm,PostProfileForm,PostImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images =Images.get_all_images()
    return render(request, 'home.html', {'images':images})

@login_required(login_url='/accounts/login/')
def  search(request):
    if 'search' in request.GET  and request.GET['search']:
        search_term = request.GET['search']
        profiles = Profiles.get_profile_by_name(search_term)
        message = f'{search_term}'
        return render (request,{'profiles':profiles,'search_term':search_term})
    else:
        message = 'Search Username'
        return render(request, 'search.html', {'message':message})

@login_required(login_url='/accounts/login/')    
def profile(request,username):
    user= User(username=username)
    profile = Profiles.filter_profile_by_id(user.id)
    title = f'{user.username} Profile'
    images = Images.get_profile_images(user.id)
    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'images':images})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('editProfile')
        else:
            form = PostProfileForm()
        return render(request,'profile/prof-edit.html',{'form':form})

def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('profile',username=request.user)
        else:
            form = PostImageForm()
        return render(request,'profile/post_images.html',{'form':form})
    
        