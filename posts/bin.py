from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views import View

# def about(request):
#     context={
#         "title": "About Page",
#     }
#     return render(request, 'about.html', context)

def services(request):
    context={
        "title": "Services Page",
    }
    return render(request, 'services.html', context)

def greet(request:HttpRequest):
    name = request.GET.get("name") or "Friend"
    return HttpResponse(f"Hello {name}")

def all_posts(request:HttpRequest):
    posts=Post.objects.all()
    return HttpResponse(str(posts))

def one_post(request:HttpRequest, post_id):
    posts=Post.objects.all()
    for post in posts:
        if post["id"] == post_id:
            return HttpResponse(str(post))
    return HttpResponse("Post Not Found")

