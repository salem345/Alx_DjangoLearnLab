from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    Includes validation to prevent future publication years.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        if attrs['publication_year'] > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return attrs


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    Includes nested serialization for related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']