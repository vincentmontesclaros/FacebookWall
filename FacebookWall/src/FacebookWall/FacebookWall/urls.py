from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'FacebookWall.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'fbwall.views.login_user'),
                       # url(r'^$', posts.views.ListPostView.as_view(),
                       #     name='post-list',),
                       # url(r'^new/$', posts.views.CreatePostView.as_view(),
                       #     name='posts-new',),
                       )
