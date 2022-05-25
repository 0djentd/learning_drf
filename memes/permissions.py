from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.request import Request

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class IsMemeAuthorPermission(permissions.DjangoObjectPermissions):
    def has_permission(self, req, view):
        logger.debug(req.user)
        logger.debug(req.user.is_staff)
        if req.user.is_staff:
            return True
        return False

    def has_object_permission(self, req, view, obj):
        logger.debug(req.user)
        logger.debug(obj.user)
        if req.user.id == obj.user.id:
            return True
        return False

