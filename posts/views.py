import datetime

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from posts.forms import NewPostForm
from posts.models import Post


class LatestPostsView(View):

    def get(self, request):
        # Retrieve last posts from database
        posts = Post.objects.filter(publication_date__lte=datetime.datetime.now()).order_by(
            '-publication_date').select_related('owner')

        # Create context
        context = {'latest_posts': posts[:5]}

        # Crete HTTP response with posts
        html = render(request, 'posts/latest.html', context)

        # Return HTP response
        return HttpResponse(html)


class PostDetailView(View):

    def get(self, request, username, pk):
        # Retrieve last posts from database
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk)

        # Create context
        context = {'post': post, 'owner': username}

        # Crete HTTP response with posts
        html = render(request, 'posts/detail.html', context)

        # Return HTP response
        return HttpResponse(html)


class NewPostView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'posts/new_post.html', context)

    def get(self, request):
        if request.user.is_authenticated is False:
            return redirect('home')

        form = NewPostForm()
        return self.render_template_with_form(request, form)

    def post(self, request):
        if request.user.is_authenticated is False:
            return redirect('home')

        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            url = form.cleaned_data.get('url')
            introduction = form.cleaned_data.get('intro')
            body = form.cleaned_data.get('body')
            publication_date = form.cleaned_data.get('pub_date')
            post = Post(owner=User.objects.get(username=request.user.username), title=title, url=url, introduction=introduction, body=body, publication_date=publication_date)
            post.save()
            url = request.GET.get('next', 'home')
            return redirect(url)

        return self.render_template_with_form(request, form)
