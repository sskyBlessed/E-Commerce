from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomModelViewSet

router = DefaultRouter()
router.register(r'custom-models', CustomModelViewSet, basename='custommodel')

urlpatterns = [
    path('', include(router.urls)),
]
