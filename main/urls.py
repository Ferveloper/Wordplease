"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from posts.api import PostsViewSet, UserPostsAPIView
from posts.views import LatestPostsView, PostDetailView, NewPostView
from users.api import UsersViewSet, BlogsListAPIView
from users.views import BlogsListView, BlogView, LoginView, LogoutView, SignupView

# API
router = SimpleRouter()
router.register('api/posts', PostsViewSet, basename='posts_api')
router.register('api/users', UsersViewSet, basename='users_api')
router.register('api/blogs', BlogsListAPIView, basename='blogs_api')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    # Blogs
    path('blogs/', BlogsListView.as_view(), name='blogs_list'),
    path('blogs/<str:username>/', BlogView.as_view(), name='user_blog'),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='user_post'),
    # Posts
    path('', LatestPostsView.as_view(), name='home'),
    path('new/', NewPostView.as_view(), name='new_post'),
    # API
    path('api/blogs/<str:username>', UserPostsAPIView.as_view(), name='user_posts')
] + router.urls

