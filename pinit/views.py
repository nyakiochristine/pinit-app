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
            
            return render(request,'profile/prof-edit.html',{'form':form})

@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('profile',username=request.user)
    else:
        form = PostImageForm()
    return render(request,'profile/post_images.html',{'form':form})
    
@login_required(login_url='/accounts/login/')
def view_single_image(request,image_id):
    image = Images.get_image_by_id(image_id)
    comments = Comment.get_comment_by_image(image_id)
    current_user = request.user
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('singleImage',image_id=image_id)
    else:
        form = PostCommentForm()
    return render(request, 'photos.html',{'image':image,'form':form,'comments':comments})


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
