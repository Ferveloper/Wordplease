import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

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
        context = {'post': post}

        # Crete HTTP response with posts
        html = render(request, 'posts/detail.html', context)

        # Return HTP response
        return HttpResponse(html)

