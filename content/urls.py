from rest_framework.routers import DefaultRouter

from content.views import ContentViewSet, ContentScoreViewSet

router = DefaultRouter()
router.register('content/score', ContentScoreViewSet, 'content-score')
router.register('content', ContentViewSet, 'content')
