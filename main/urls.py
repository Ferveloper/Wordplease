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

from posts.views import LatestPostsView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    # Blogs
    # path('blogs/', blogs_list, name='blogs_list'),
    # path('blogs/<str:username>/', user_blog, name='user_blog'),
    # path('blogs/<str:username>/<int:pk>', user_post, name='user_post'),
    # Posts
    path('', LatestPostsView.as_view(), name='home'),
    # path('new/', new_post, name='new_post')
]
