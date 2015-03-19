from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from posts.models import Post


class ListPostView(ListView):
    model = Post
    template_name = 'posts_list.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse('posts_list')
