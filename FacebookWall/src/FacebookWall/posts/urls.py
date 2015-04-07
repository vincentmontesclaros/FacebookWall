from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from posts import views

urlpatterns = patterns(
    '',
    url(r'^login/$', 'django.contrib.auth.views.login', {
     'template_name': 'index.html'}, name='login'),
    url(r'^logout/$', login_required(
     views.Logout.as_view()), name='logout'),
    url(r'^feed/$', login_required(
     views.Posts.as_view()), name='feed'),
    url(r'^$', login_required(
     views.Posts.as_view())),
    url('^register/', CreateView.as_view(
     template_name='register.html',
     form_class=UserCreationForm,
     success_url='/feed'
    ), name='register'),
    url(r'^post/$', login_required(
     views.CreatePost.as_view()), name='post'),
    url(r'^post/(?P<post_id>\d+)/delete/$', login_required(
     views.RemovePost.as_view()), name='delete'),
    url(r'^post/(?P<post_id>\d+)/like/$', login_required(
     views.LikePost.as_view()), name='like'),
    url(r'^index/$', views.Index.as_view(), name='index'),
    url(r'^feed/post/(?P<post_id>\d+)/edit/$', login_required(
         views.EditPost.as_view()), name='edit'),
                       )
