from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return view.action == 'retrieve' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return obj.publication_date <= timezone.now() or obj.owner == request.user or request.user.is_superuser

        return obj.owner == request.user or request.user.is_superuser
