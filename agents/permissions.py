from rest_framework import permissions


class IsRealAgent(permissions.BasePermission):
    def has_object_permission(self, request, view, agent):
        if request.user:
            return agent.name == request.user
        return False
