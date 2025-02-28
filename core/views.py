from django.shortcuts import render
from .models import Post
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        'title' : 'Clean Blog',
        'page_title': 'Clean Blog',
        'page_subtitle': 'A Blog Theme by Start Bootstrap',
        'back_image' : 'home-bg',
        'posts': posts
    }
    return render(request, 'home.html', context)

def about_page(request):
    context = {
        'title': 'About Us',
        'page_title': 'About Us',
        'page_subtitle': 'Learn more about us',
        'back_image' : 'about-bg'
    }
    return render(request, 'about.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    context = {
        'title' : 'Post',
        'page_title' : post.title,
        'post': post
    }
    return render(request, 'post_detail.html', context)

