from rest_framework import serializers
from .models import FocusLog, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class FocusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FocusLog
        fields = '__all__'