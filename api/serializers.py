from rest_framework import serializers

from api.models import Book
from api.validators import check_title_length   


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'is_active')
    
    # field level valdiation
    def validate_description(self, value):
        print(value)
        if len(value) < 5:
            message = "Description must be more than 5 chars !"
            raise serializers.ValidationError(message)
        return value
    
    def validate(self, attrs):
        if attrs['title'] == attrs['description']:
            message = "Title and Description cant be same !"
            raise serializers.ValidationError(message)
        return attrs