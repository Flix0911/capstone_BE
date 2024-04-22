from rest_framework import generics
from memory.models import GoodMemory, BadMemory, Image
from memory.serializers import GoodMemorySerializer, BadMemorySerializer, ImageSerializer
from rest_framework import viewsets

class GoodMemoryViewSet(viewsets.ModelViewSet):
    queryset = GoodMemory.objects.all()
    serializer_class = GoodMemorySerializer
    
class BadMemoryViewSet(viewsets.ModelViewSet):
    queryset = BadMemory.objects.all()
    serializer_class = BadMemorySerializer
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer