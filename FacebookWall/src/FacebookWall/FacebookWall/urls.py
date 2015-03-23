from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login
from posts import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'FacebookWall.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'posts.views.logout_page'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # url(r'^$', posts.views.ListPostView.as_view(),
                       #     name='post-list',),
                       # url(r'^new/$', posts.views.CreatePostView.as_view(),
                       #     name='posts-new',),
                       )
