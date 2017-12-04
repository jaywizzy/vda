from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    photo = models.ImageField(upload_to="profile_photos", blank=True)
    middle_name = models.CharField(max_length = 100, blank=True, default='')
    hamlet_name = models.CharField(max_length = 100, blank=True, default='')
    ward_name = models.CharField(max_length = 100, blank=True, default='')
    district = models.CharField(max_length = 100, blank=True, default='')
    address = models.CharField(max_length = 100, blank=True, default='')
    occupation = models.CharField(max_length = 100, blank=True, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length = 100, blank=True, default='')
    educational_qualification = models.CharField(max_length = 100, blank=True, default='')

    def __str__(self):
        return '%s' %(self.user.first_name)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)



