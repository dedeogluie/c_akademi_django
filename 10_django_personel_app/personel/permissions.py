from rest_framework import permissions


class IsStaffOrReadOnly(permissions.IsAdminUser):

    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user and request.user.is_staff)
        

class IsOwnerOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method == 'GET':
                return True
            return bool(request.user.is_staff and (obj.user == request.user))