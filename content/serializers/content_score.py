from rest_framework import serializers

from content.models import ContentScore


class ContentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentScore
        fields = ('content', 'score',)
