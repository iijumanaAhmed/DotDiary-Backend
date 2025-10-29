from rest_framework import serializers
from .models import ToDoList, Distraction, Tag, FocusLog

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class DistractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distraction
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class FocusLogSerializer(serializers.ModelSerializer):
    distraction = DistractionSerializer(many=True, read_only=True)
    
    class Meta:
        model = FocusLog
        fields = '__all__'