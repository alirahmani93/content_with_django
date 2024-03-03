from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from content.models.content import Content
from django.core import validators
from django.utils.translation import gettext_lazy as _

from content.querysets.content_score_queryset import ContentScoreManager, ContentScoreQuerySet
from utilities import BaseModel, WithUserMixin


class ContentScore(WithUserMixin, BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('محتوا'))
    score = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)],
        verbose_name=_('امتیاز'))

    objects = ContentScoreManager.from_queryset(ContentScoreQuerySet)()

    class Meta:
        unique_together = ("user", "content")

    def __str__(self):
        return f"{self.user} give {self.score} to {self.content}"
