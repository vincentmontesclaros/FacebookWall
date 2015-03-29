from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login
from posts import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'FacebookWall.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('posts.urls', namespace="posts")),
                       )
