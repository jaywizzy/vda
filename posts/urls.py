from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'posts/$', create_post, name='create_post'),
    url(r'posts/comment/(?P<pk>\d+)/$', comments, name='comments'),
]
