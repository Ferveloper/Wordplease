import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from users.forms import LoginForm, SignupForm


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


class LoginView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return self.render_template_with_form(request, form)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return self.render_template_with_form(request, form)


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')


class SignupView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignupForm()
        return self.render_template_with_form(request, form)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('fname')
            last_name = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            User.objects.create_user(username=username, email= email, password=password, first_name=first_name, last_name=last_name)
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return self.render_template_with_form(request, form)
