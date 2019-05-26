from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer, WriteUserSerializer, BlogSerializer


class UsersViewSet(GenericViewSet):

    permission_classes = [UserPermission]

    def create(self, request):
        serializer = WriteUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = WriteUserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogsListAPIView(ListAPIView):
#
#     # queryset = User.objects.all()
#     serializer_class = BlogSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['username']
#     ordering_fields = ['first_name']
#
#     def get_queryset(self):
#         users = User.objects.all().exclude(username='admin')
#         queryset = []
#         for user in users:
#             queryset.append({
#                 'first_name' : user.first_name,
#                 'last_name' : user.last_name,
#                 'username' : user.username,
#                 'url' : '/blogs/' + user.username
#             })
#         return queryset

class BlogsListAPIView(GenericViewSet):

    def list(self, request):
        users = User.objects.all().exclude(username='admin')

        if 'search' in request.query_params:
            search = request.query_params.get('search')
            users = users.filter(username__contains=search)

        blogs = []
        for user in users:
            blogs.append({
                'name': user.first_name + ' ' + user.last_name,
                'username': user.username,
                'url': '/blogs/' + user.username + '/'
            })

        if ('ordering' in request.query_params) and (request.query_params.get('ordering') in ['name', '-name']):
            if request.query_params.get('ordering')[0] == '-':
                reverse = True
            else:
                reverse = False
            blogs = sorted(blogs, key = lambda k:k['name'], reverse=reverse)

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)