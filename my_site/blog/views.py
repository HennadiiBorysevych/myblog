from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def starting_page(req):
    return render(req,'blog/index.html')
    

def posts(req):
    return render(req, 'blog/all-posts.html')

def post_detaild(req,slug):
    return render(req, 'blog/post-detail.html')
