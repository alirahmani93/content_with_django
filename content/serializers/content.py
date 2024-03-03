from rest_framework import serializers

from content.models import Content


class ContentSerializer(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()
    count_score = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ('title', 'average_score', 'count_score')

    def get_average_score(self, obj):
        if obj:
            return obj.average_score
        return None

    def get_count_score(self, obj):
        if obj:
            return obj.count_score
        return None
