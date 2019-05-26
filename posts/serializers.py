from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'introduction', 'publication_date']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'introduction', 'body', 'publication_date', 'creation_date', 'modification_date', 'categories', 'owner']
        read_only_fields = ['id', 'creation_date', 'modification_date', 'owner']
