from rest_framework import serializers
from .models import FocusLog

class FocusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FocusLog
        fields = '__all__'