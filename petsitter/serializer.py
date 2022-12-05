from rest_framework import serializers
from .models import Document, Location, ImgDocument


class DocumentSerializer(serializers.ModelSerializer):
    uploadedFile = serializers.FileField(use_url=True)
    dateTimeOfUpload = serializers.DateTimeField('%m-%d %H:%M')

    class Meta:
        model = Document
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    uploadedImg = serializers.ImageField(use_url=True)

    class Meta:
        model = ImgDocument
        fields = ('title', 'uploadedImg')