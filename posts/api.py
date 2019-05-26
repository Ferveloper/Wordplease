import datetime

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostsViewSet(ModelViewSet):

    permission_classes = [PostPermission]
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'introduction']
    # ordering_fields = ['title', 'publication_date']

    def get_queryset(self):
        queryset = Post.objects.select_related('owner').order_by('-publication_date')
        # if (not self.request.user.is_authenticated) or (not self.request.user == self.request.data):
        #     queryset = queryset.filter(publication_date__lte=datetime.datetime.now())
        return queryset

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        return Response({"detail": "Method \"GET\" not allowed."}, status=403)
