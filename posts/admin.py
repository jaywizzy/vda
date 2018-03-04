from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['starter', 'content']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'reply', 'created_by']

admin.site.register(Comment, CommentAdmin)
