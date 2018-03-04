from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.conf import settings
from .forms import SignupForm, UserProfileForm  ,ProfileForm, StaffForm
from .models import Profile
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from app.models import User
from django.contrib import messages
from posts.models import Post
from posts.models import *
from posts.forms import *
# User = settings.AUTH_USER_MODEL


# Create your views here.

# def test(request):
#     posts = Post.objects.all()
#     return render(request, 'test.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(edit_profile)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def register_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            User.is_staff == True
            a.save()
            return HttpResponse('YEAH, STAFF CREATED')
    else:
        form = StaffForm()
    return render(request, 'accounts/staff_signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

def search(request):
    # user_list = User.objects.all()
    query = request.GET.get('q')
    user_list = User.objects.all()

    if query:
        user_list = user_list.filter(
        Q(first_name__icontains=query)|
        Q(last_name__icontains=query)|
        Q(profile__middle_name__icontains=query)|
        Q(profile__district__icontains=query)|
        Q(profile__occupation__icontains=query)|
        Q(profile__ward_name__icontains=query)|
        Q(profile__hamlet_name__icontains=query)|
        Q(profile__district__icontains=query)
        )
    return render(request, 'search.html', {"result": user_list })

# @login_required
def home(request):
    # if request.user.is_superuser:
    query_list = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST or None)                                                                                                                                                                                                                                                                                                                                                                                 
        photo_form = PhotoForm(request.FILES or None)
        if photo_form.is_valid():
            # photo = photo_form.save(commit=False)
            # photo.image = image
            # photo.user = reuest.user
            # photo_form.save()
            # post = form.save(commit=False)
            # photo.user = request.user
            # post.user = request.user
            photo_form.save()
            # post.save()

            return redirect('/')

    else:
        form = PostForm()
        photo_form = PhotoForm()

    return render(request, 'home.html', {'post': query_list, 'form': form, 'photo': photo_form})

def user_list(request):

    query = request.GET.get('q')
    user_list = User.objects.all()
    if query:
        user_list = user_list.filter(
        Q(first_name__icontains=query)|
        Q(last_name__icontains=query)|
        Q(profile__middle_name__icontains=query)|
        Q(profile__district__icontains=query)|
        Q(profile__occupation__icontains=query)|
        Q(profile__ward_name__icontains=query)|
        Q(profile__hamlet_name__icontains=query)|
        Q(profile__district__icontains=query)
        )
    return render(request, 'user_list.html', {'result': user_list})
def user_details(request, id):
    print (request.user.id)
    instance = get_object_or_404( User, id=id)
    context = {
        'instance': instance
    }
    return render(request, "user_detail.html", context)

@login_required
def edit_profile(request):

    if request.method == "POST":
        u_form = UserProfileForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid() or u_form.is_valid():
            p_form.save()
            u_form.save()
            # messages.success(request, 'your profile was successfully updated')
            return redirect('/profile/')
        else:
            messages.error(request, 'please correct the error below')
    else:
        u_form = UserProfileForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    return render(request, "accounts/edit_profile.html", {
        "u_form": u_form,
        "p_form": p_form,
    })
