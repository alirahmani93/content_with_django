from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from content.models import Content
from content.serializers import ContentSerializer


class ContentViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.is_available()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        authentication is required

        :return: [{'title': str, 'average_score': float, 'count_score': int}]
        """
        qs = self.get_queryset().ordered_avg_count_score()
        return Response(self.serializer_class(qs, many=True).data)
