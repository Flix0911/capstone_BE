from rest_framework import serializers
from memory.models import GoodMemory, BadMemory, Image

class GoodMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodMemory
        fields = ('id', 'title', 'weather', 'comment', 'attendents', 'location', 'season', 'country', 'date', 'image')

class BadMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BadMemory
        fields = ('id', 'title', 'weather', 'comment', 'attendents', 'location', 'season', 'country', 'date', 'image')
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']