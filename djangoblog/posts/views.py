from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def home(request):

    posts = BlogPost.objects.order_by('publication_date')


    return render(request, 'posts/home.html', {'posts': posts})