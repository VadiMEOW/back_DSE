from rest_framework import serializers
from .models import Camera, ClusterUnit, Processing, DetectedObjectTypes, ObjectsDetectionLogs


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class ClusterUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterUnit
        fields = '__all__'

class ProcessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processing
        fields = '__all__'

class ObjectsDetectionLogsSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='location.location')
    type = serializers.CharField(source='type.type')
    class Meta:
        model = ObjectsDetectionLogs
        fields = '__all__'
