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
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance