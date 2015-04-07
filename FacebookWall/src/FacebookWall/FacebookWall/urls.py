from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import admin


from posts import views

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('posts.urls', namespace="posts")),
                       )
