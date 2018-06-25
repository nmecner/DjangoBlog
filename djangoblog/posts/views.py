from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def home(request):

    posts = BlogPost.objects.order_by('-publication_date')


    return render(request, 'posts/home.html', {'posts': posts})

def posts_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'posts/posts_detail.html', {'post': post})
