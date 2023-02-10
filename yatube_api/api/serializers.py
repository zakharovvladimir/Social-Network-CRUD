"""API Serializers."""
from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Post Serializer Meta."""

        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Group Serializer."""

    class Meta:
        """Group Serializer Meta."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Comment Serializer Meta."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
