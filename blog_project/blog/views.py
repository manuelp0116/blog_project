from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


## Registration form using Django build in form for this
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'There was an error with your registration. Please check the form and try again.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  # Updated from 'test/registration.html'

def home(request):
    return render(request, 'home.html')

@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'user_posts.html', {'posts': posts})

def main_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})  # Updated template path

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main_page')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})  # Updated from 'test/create_post.html'

@login_required
def user_hub(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'user_hub.html', {'posts': posts})  # Updated from 'test/user_hub.html'

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_hub')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})  # Updated from 'test/edit_post.html'

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})  # Updated from 'test/delete_post.html'

def logout_screen(request):
    logout(request)
    return render(request, 'login.html')  # Updated from 'test/logout.html'