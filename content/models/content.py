from django.db import models
from django.utils.translation import gettext_lazy as _

from content.querysets.content_queryset import ContentQuerySet, ContentManager
from utilities import BaseModel, WithUserMixin


class Content(WithUserMixin, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('عنوان'))
    text = models.TextField(verbose_name=_('متن'))

    objects = ContentManager.from_queryset(ContentQuerySet)()

    def __str__(self):
        return f"{self.user} write {self.title}"
