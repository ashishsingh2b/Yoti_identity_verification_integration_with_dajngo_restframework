from rest_framework import serializers

class CreateYotiSessionSerializer(serializers.Serializer):
    user_tracking_id = serializers.CharField(max_length=255)
