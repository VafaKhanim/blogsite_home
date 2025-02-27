from django.shortcuts import render
from .models import Post
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context_home = {
        'title' : 'Clean Blog',
        'page_title': 'Clean Blog',
        'page_subtitle': 'A Blog Theme by Start Bootstrap',
        'back_image' : 'home-bg'
    }

    # posts və context_home birləşdirilir
    context = {
        'posts': posts,
        **context_home,  # context_home ilə posts birləşdirilir
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
