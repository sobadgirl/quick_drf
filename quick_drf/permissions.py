from rest_framework import permissions
from app.models import User


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        owner = getattr(obj, 'owner', None)
        return owner is not None and owner == request.user


class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User):
        return request.user == user
