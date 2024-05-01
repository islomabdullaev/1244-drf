from rest_framework import serializers

from api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=24)
    description = serializers.CharField()
    is_active = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)