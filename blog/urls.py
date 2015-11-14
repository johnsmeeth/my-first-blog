from django.conf.urls import url
from . import views

urlpatterns = [
    # Match with empty string: for this match with http://localhost:8000/
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
