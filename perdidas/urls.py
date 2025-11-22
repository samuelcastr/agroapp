from rest_framework import routers
from django.urls import path, include
from perdidas.views import PerdidaViewSet, CausaPerdidaViewSet

router = routers.DefaultRouter()
router.register(r"perdidas", PerdidaViewSet)
router.register(r"causas-perdida", CausaPerdidaViewSet)

urlpatterns = router.urls