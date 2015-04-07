from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from posts.forms import UserRegistrationForm
from posts.models import Post


class Login(TemplateView):
    def get(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('feeds:feed'))


class Posts(TemplateView):
    template_name = 'feed.html'

    def get(self, request):
        if request.user.is_authenticated():
            latest_post_list = Post.objects.order_by('-pub_date')[:10]
            user = request.user
            liked_posts = Post.objects.all().filter(likers=request.user)
            return self.render_to_response({
                'latest_post_list': latest_post_list,
                'user': user,
                'liked_posts': liked_posts,
            })
        else:
            return redirect(reverse('posts:index'))


class IndexView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('posts:feed'))
        else:
            return self.render_to_response({'login_form': forms.LoginForm()})


class CreatePost(TemplateView):
    def post(self, request):
        if request.POST['content'] != '':
            post = Post.objects.create(
                content=request.POST['content'],
                author=request.user
            )
        return redirect(reverse('posts:feed'))


class EditPost(TemplateView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if request.POST['new_content'] != '':
            post.content = request.POST['new_content']
            post.save()
        return redirect(reverse('posts:feed'))


class RemovePost(TemplateView):
    template_name = 'feed.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect(reverse('posts:feed'))


class LikePost(TemplateView):
    template_name = 'feed.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.likers.filter(username=request.user).exists():
            post.likers.remove(request.user)
        else:
            post.likers.add(request.user)
        return redirect(reverse('posts:feed'))


class RegisterUser(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                return redirect(reverse('posts:register_success'))
        else:
            form = UserRegistrationForm()
        return render(request, 'index.html', {'form': form})


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                return redirect(reverse('posts:register_success'))
        else:
            form = UserRegistrationForm()
        return render(request, 'index.html', {'form': form})


class Logout(TemplateView):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')
