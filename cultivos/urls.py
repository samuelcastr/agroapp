from rest_framework.routers import DefaultRouter
from .views import CultivoViewSet

router = DefaultRouter()
router.register(r'cultivos', CultivoViewSet, basename='cultivos')

urlpatterns = router.urls
