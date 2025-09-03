from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Only allow the creator of a book to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions allowed for everyone
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Write permissions only for the user who created the object
        return obj.author == request.user.username
