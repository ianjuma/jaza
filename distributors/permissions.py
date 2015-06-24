from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, distributor):
        if request.user:
            return distributor.username == request.user
        return False
