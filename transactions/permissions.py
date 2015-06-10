from rest_framework import permissions


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, transaction):
        if request.user:
            return transaction == request.user
        return False
