from rest_framework import permissions


class IsRealDistributor(permissions.BasePermission):
    def has_object_permission(self, request, view, distributor):
        if request.user:
            return distributor.name == request.user
        return False
