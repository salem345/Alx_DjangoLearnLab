from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # السماح للقراءة للجميع
        if request.method in permissions.SAFE_METHODS:
            return True
        # الكتابة، التعديل، الحذف بس للـ Admin
        return request.user and request.user.is_staff