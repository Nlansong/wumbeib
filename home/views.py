from django.shortcuts import render
from blog.models import PostModel, Tag

# Create your views here.

def home(request):
    posts = PostModel.objects.all()[0:6]
    
    context = {
        'title': 'Latest Posts',
        'posts':posts
    }
    
    return render(request, 'home/home.html', context)
