from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'test/registration.html', {'form': form})

def home(request):
    return render(request, 'homepage.html')

def post_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.all().order_by('-created_at') #getch all post from database
    return render(request, 'posts.html', {'posts': posts})

def main_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'test/main_page.html', {'posts': posts})

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
    return render(request, 'test/create_post.html', {'form': form})

@login_required
def user_hub(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'test/user_hub.html', {'posts': posts})

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
    return render(request, 'test/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('user_hub')
    return render(request, 'test/delete_post.html', {'post': post})

def logout_screen(request):
    logout(request)
    return render(request, 'test/logout.html')