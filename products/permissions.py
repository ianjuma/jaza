from rest_framework import permissions


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, product):
        if request.user:
            return product.owner == request.user
        return False
