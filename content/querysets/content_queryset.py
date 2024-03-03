from django.db.models import Avg, Count

from utilities import BaseQuerySet, BaseManager


class ContentQuerySet(BaseQuerySet):

    def score_avg(self):
        return self.annotate(average_score=Avg("contentscore__score"))

    def score_count(self):
        return self.annotate(count_score=Count("contentscore"))

    def ordered_avg_count_score(self):
        return self.score_avg().score_count().order_by('-count_score', '-average_score')


class ContentManager(BaseManager):
    pass
