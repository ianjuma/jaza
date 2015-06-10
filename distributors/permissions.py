from rest_framework import permissions


class IsRealDistributor(permissions.BasePermission):
    def has_object_permission(self, request, view, distributor):
        if request.user:
            return distributor.phone_number == request.user
        return False
