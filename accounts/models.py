from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.
User = settings.AUTH_USER_MODEL
gender = (
    ('m', 'Male'),
    ('f', 'Female')
)
diasbilities = (
    ('n', 'none'),
    ('s', 'specify')
)
status = (
    ('e', 'employed'),
    ('u', 'unemployed')
)
class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile')
    slug = models.SlugField(unique=True, blank=True, null=True, default='')
    middle_name = models.CharField(max_length = 100, blank=True, default='')
    village = models.CharField(max_length = 100, blank=True, default='')
    ward = models.CharField(max_length = 100, blank=True, default='')
    district = models.CharField(max_length = 100, blank=True, default='')
    address = models.CharField(max_length = 100, blank=True, default='')
    home_address = models.CharField(max_length = 100, blank=True, default='')
    occupation = models.CharField(max_length = 100, blank=True, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length = 100, blank=True, default='')
    educational_qualification = models.CharField(max_length = 100, blank=True, default='')
    gender = models.CharField(max_length=100, choices=gender, blank=True)
    diasbilities = models.CharField(max_length=100, choices=diasbilities, blank=True)
    employement_status = models.CharField(max_length=100, choices=status, blank=True)
    photo = models.ImageField(upload_to="profile_photos", blank=True)
    

    # objects = ProfileManager()

    def __str__(self):
        return '%s' %(self.user.first_name)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

def pre_save_profile_signal(sender, instance, *args, **kwargs):
    slug = slugify(instance.user.last_name+instance.user.first_name+str(instance.user.id))
    exists = Profile.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_profile_signal, sender=Profile)
