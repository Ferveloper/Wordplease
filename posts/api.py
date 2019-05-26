import datetime

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostsViewSet(ModelViewSet):

    permission_classes = [PostPermission]

    def get_queryset(self):
        queryset = Post.objects.select_related('owner').order_by('-publication_date')
        return queryset

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        return Response({"detail": "Method \"GET\" not allowed."}, status=403)


class UserPostsAPIView(ListAPIView):

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'introduction']
    ordering_fields = ['title', 'publication_date']
    ordering = ['-publication_date']
    serializer_class = PostListSerializer

    def get_queryset(self):

        user = self.request.user
        username = self.kwargs.get('username')
        query_set = Post.objects.filter(owner__username=username).select_related('owner')

        if not user.is_authenticated or (user.username != username and not user.is_superuser):
            query_set = query_set.filter(publication_date__lte=datetime.datetime.now())

        return query_set
