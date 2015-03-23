from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView
from posts.models import Post
from django.http import HttpResponseRedirect, HttpResponse


def logout_page(request):
    logout(request)
    # Redirect to a success page.
    # return render(request, 'login.html')
    return HttpResponseRedirect('/')


# def index(request):
#     # pass posts here
#     latest_post_list = Post.objects.order_by('-pub_date')[:10]
#     # output = ', '.join([p.content for p in latest_post_list])
#     # return HttpResponse(output)

#     # using render
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'feed.html', context)


class IndexView(ListView):
    template_name = 'feed.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """ Return the last ten published posts. """
        return Post.objects.order_by('-pub_date')[:10]


# class CreatePostView(CreateView):
#     model = Post
#     template_name = 'edit_post.html'

#     def get_success_url(self):
#         return reverse('feed')
