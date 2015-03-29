from django.conf.urls import patterns, include, url
from posts import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$',
                           login_required(views.IndexView.as_view()),
                           name='index'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {
                            'template_name': 'login.html'}, name='login'),
                       url(r'^logout/$', 'posts.views.logout_page'),
                       url(r'^feed/$', login_required(
                                      views.PostsView.as_view()), name='feed'),
                       url(r'^register/$', 'posts.views.register_user'),
                       url(r'^register_success/$',
                           'posts.views.register_success'),
                       url(r'^post/$', login_required(
                          views.CreatePostView.as_view()), name='post'),
                       url(r'^post/(?P<post_id>\d+)/delete/$', login_required(
                          views.RemovePostView.as_view()), name='delete'),
                       url(r'^post/(?P<post_id>\d+)/like/$', login_required(
                          views.LikePostView.as_view()), name='like'),
                       url(r'^post/(?P<post_id>\d+)/edit/$', login_required(
                          views.EditPostView.as_view()), name='edit'),
                       )
