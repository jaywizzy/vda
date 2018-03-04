from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from app.models import User
from .models import Profile
from django.contrib.admin.widgets import AdminDateWidget
# User = settings.AUTH_USER_MODEL


class SignupForm(UserCreationForm):
    email = forms.CharField(max_length = 254, required = True, widget=forms.EmailInput())
    first_name = forms.CharField(max_length = 254, required = True)
    last_name = forms.CharField(max_length = 254, required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class StaffForm(UserCreationForm):
    email = forms.CharField(max_length = 254, required = True, widget=forms.EmailInput())
    first_name = forms.CharField(max_length = 254, required= True)
    last_name = forms.CharField(max_length = 254, required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    # date_of_birth = forms.DateField(widget=forms.SelectDateWidget())
    date_of_birth = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ['user', 'slug' ]



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        # exclude = ['password1', 'password2']
