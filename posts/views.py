from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from app.models import User
from .forms import *
from django.http import HttpResponse
# Create your views here.

def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.starter = request.user
            post.save()
            return HttpResponse('YEAH!!! Post was created successfully')

    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def comments(request, pk):
    comment = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.reply = comment
            comment.created_by = request.user
            return HttpResponse('YOUR COMMENT HAS BEEN POSTED')

    else:
        form = CommentForm()
    return render(request, 'comments.html', {'form': form})
