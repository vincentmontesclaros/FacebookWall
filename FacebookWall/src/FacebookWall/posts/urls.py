from django.conf.urls import patterns, include, url
from posts import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^$',
                           login_required(views.IndexView.as_view()),
                           name='index'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {
                            'template_name': 'login.html'}, name='login'),
                       url(r'^logout/$', login_required(
                           views.Logout.as_view()), name='logout'),
                       url(r'^feed/$', login_required(
                           views.Posts.as_view()), name='feed'),
                       url(r'^register/$', 'posts.views.register_user'),
                       url(r'^register_success/$',
                           'posts.views.register_success'),
                       url(r'^post/$', login_required(
                          views.CreatePost.as_view()), name='post'),
                       url(r'^post/(?P<post_id>\d+)/delete/$', login_required(
                          views.RemovePost.as_view()), name='delete'),
                       url(r'^post/(?P<post_id>\d+)/like/$', login_required(
                          views.LikePost.as_view()), name='like'),
                       url(r'^feed/post/(?P<post_id>\d+)/edit/$', login_required(
                          views.EditPost.as_view()), name='edit'),
                       )
