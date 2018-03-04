from django.db import models
from app.models import User
# Create your models here.

class Post(models.Model):
    starter = models.ForeignKey(User, related_name = 'posts')
    content = models.TextField(max_length=4000, blank=True)
    date_created = models.DateTimeField(auto_now = False, auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%s, %s' %(self.starter, self.content)
class Photo(models.Model):
    user = models.ForeignKey(User, related_name = 'photos', null=True)
    image = models.ImageField(upload_to = 'uploads')
    date_created = models.DateTimeField(auto_now = False, auto_now_add = True)


class Comment(models.Model):
    reply = models.TextField(max_length=1500)
    created_by = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    image = models.ImageField(upload_to='uploads', blank=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, %s' %(self.post, self.message)
