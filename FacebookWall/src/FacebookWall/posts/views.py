from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView
from posts.models import Post
from django.http import HttpResponseRedirect


def logout_page(request):
    logout(request)
    # Redirect to a success page.
    # return render(request, 'login.html')
    return HttpResponseRedirect('/')


def index(request):
    # pass posts here
    return render(request, 'feed.html')


class ListPostView(ListView):
    model = Post
    template_name = 'feed.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse('feed')
