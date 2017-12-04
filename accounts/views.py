from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .forms import SignupForm, UserProfileForm  ,ProfileForm
from .models import Profile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from app.models import User
from django.contrib import messages
# User = settings.AUTH_USER_MODEL


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
# def edit_user(request):
#     user = request.user
#     user_form = UserProfileForm(instance=request.user)
#
#     ProfileInlineFormset = inlineformset_factory(User, Profile,
#                                                  fields=('photo', 'middle_name', 'ward_name', 'hamlet_name', 'district', 'address',
#                                                          'occupation', 'date_of_birth', 'phone_number', 'educational_qualification'))
#     formset = ProfileInlineFormset(instance=user)
#
#     if request.user.is_authenticated() and request.user.id == user.id:
#         if request.method == "POST":
#             user_form = UserProfileForm(request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
#
#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=request.user.get_profile())
#
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return redirect('/')
#
#         return render(request, "acct_update.html", {
#             "form": user_form,
#             "formset": formset,
#         })
#     else:
#         raise PermissionDenied
#

@login_required
def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html')



@login_required
def edit_profile(request):

    if request.method == "POST":
        u_form = UserProfileForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'your profile was successfully updated')
            return redirect('/')
        else:
            messages.error(request, 'pleas correct the error below')
    else:
        u_form = UserProfileForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    return render(request, "edit_profile.html", {
        "u_form": u_form,
        "p_form": p_form,
    })