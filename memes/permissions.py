from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.request import Request


class IsMemeAuthorPermission(permissions.DjangoObjectPermissions):
    def has_permission(self, req, view):
        if req.user.is_staff:
            return True
        return False

    def has_object_permission(self, req, view, obj):
        print(req.user)
        print(obj.user)
        if req.user.id == obj.user.id:
            print("ok bro go")
            return True
        print("gtfo")
        return False

