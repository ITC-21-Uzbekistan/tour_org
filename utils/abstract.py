from django.db import models

from auth_user.models import User


class AbstractModel(models.Model):
    is_delete = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                   related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', blank=True, null=True, default=None)

    class Meta:
        abstract = True
