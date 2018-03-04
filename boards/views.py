from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def new_board(request):
    # if request.user.is_staff:
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/')
    else:
        form = BoardForm()
    return render(request, 'board.html', {'form': form})