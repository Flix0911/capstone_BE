from django.urls import path
from .views import BadMemoryViewSet, GoodMemoryViewSet, ImageViewSet
from memories.memory import views

urlpatterns = [
    path("badmemory/", views.BadMemoryViewSet.as_views(), name='badmemory'),
]
