from rest_framework.permissions import BasePermission

from apps.models import User

class UserLoginPermission(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user,User)