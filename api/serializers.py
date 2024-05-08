from rest_framework import serializers

from api.models import Book
from api.validators import check_title_length   


class BookSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=24, validators=[check_title_length])
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
    
    # def validate_description(self, value):
    #     print(value)
    #     if len(value) < 5:
    #         message = "Description must be more than 5 chars !"
    #         raise serializers.ValidationError(message)
    #     return value
    
    # def validate(self, attrs):
    #     if attrs['title'] == attrs['description']:
    #         message = "Title and Description cant be same !"
    #         raise serializers.ValidationError(message)
    #     return attrs