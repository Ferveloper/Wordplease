import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View


class BlogsListView(View):

    def get(self, request):
        # Retrieve users from database
        users = User.objects.all().exclude(username='admin')

        # Create context
        context = {'blogs': users}

        # Crete HTTP response with posts
        html = render(request, 'users/blogs.html', context)

        # Return HTP response
        return HttpResponse(html)


class BlogView(View):

    def get(self, request, username):
        # Retrieve users from database
        owner = get_object_or_404(User, username=username)
        blog_posts = owner.posts.filter(publication_date__lte=datetime.datetime.now()).order_by(
            '-publication_date')

        # Create context
        context = {'owner': owner,
                   'blog_posts': blog_posts}

        # Crete HTTP response with posts
        html = render(request, 'users/blog_posts.html', context)

        # Return HTP response
        return HttpResponse(html)
