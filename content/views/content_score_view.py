import rest_framework.status
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from content.models import ContentScore
from content.serializers import ContentScoreSerializer


class ContentScoreViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ContentScoreSerializer
    queryset = ContentScore.objects.is_available()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        authentication is required
        body: {"content": int, "score": int}

        :return: {"content": int, "score": int}
        """
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        valid_data = serializer.validated_data
        score, is_create = ContentScore.objects.update_or_create(
            user=self.request.user, content=valid_data['content'],
            defaults={'score': valid_data['score']}
        )

        status_code = status.HTTP_201_CREATED if is_create else status.HTTP_200_OK
        return Response(self.serializer_class(score).data, status=status_code)
