from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(request.user.is_authenticated)
        return bool(request.user.is_staff)


