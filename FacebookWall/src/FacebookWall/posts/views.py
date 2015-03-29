from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from posts.models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from posts import forms


class PostsView(TemplateView):
    template_name = 'feed.html'

    def get(self, request):
        if request.user.is_authenticated():
            latest_post_list = Post.objects.order_by('-pub_date')[:10]
            user = request.user
            return self.render_to_response({
                'latest_post_list': latest_post_list,
                'user': user,
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


class CreatePostView(TemplateView):
    def post(self, request):
        if request.POST['content'] != '':
            post = Post.objects.create(
                content=request.POST['content'],
                author=request.user
            )
        latest_post_list = Post.objects.order_by('-pub_date')[:10]
        return redirect(reverse('posts:feed'))


class EditPostView(TemplateView):
    def post(self, request):
        # TODO
        bla


class RemovePostView(TemplateView):
    template_name = 'feed.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        latest_post_list = Post.objects.order_by('-pub_date')[:10]
        return redirect(reverse('posts:feed'))


class LikePostView(TemplateView):
    template_name = 'feed.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        # check if the current user has already liked this post
        likers = post.likers.all()


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


def logout_page(request):
    logout(request)
    # Redirect to a success page.
    # return render(request, 'login.html')
    return HttpResponseRedirect('/')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect(reverse('feeds:feed'))

# def get_queryset(self):
#     """ Return the last ten published posts. """
#     return Post.objects.order_by('-pub_date')[:10]

# class CreatePostView(CreateView):
#     model = Post
#     template_name = 'edit_post.html'

#     def get_success_url(self):
#         return reverse('feed')
