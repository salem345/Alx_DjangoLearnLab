from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()