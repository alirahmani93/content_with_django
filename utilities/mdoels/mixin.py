from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class WithUserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('کاربر'))

    class Meta:
        abstract = True
