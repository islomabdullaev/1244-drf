from rest_framework import serializers

# validator
def check_title_length(value):
    if len(value) < 5:
        message = "Title must be more than 5 chars !"
        raise serializers.ValidationError(message)
    return value