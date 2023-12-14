from rest_framework import serializers
from .models import (
    DetectedObjectType, 
    ObjectsDetectionLog,
)


class ObjectsDetectionLogSerializer(serializers.ModelSerializer):
    start_datestamp = serializers.DateTimeField(write_only=True, required=False)
    end_datestamp = serializers.DateTimeField(write_only=True, required=False)

    class Meta:
        model = ObjectsDetectionLog
        fields = '__all__'

class DetectedObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectedObjectType
        fields = '__all__'
