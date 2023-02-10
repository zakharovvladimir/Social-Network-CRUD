"""API views."""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermission
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment


class PostViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, PATCH, DELETE."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def perform_create(self, serializer):
        """Post modification."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """GET."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, PATCH, DELETE."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def perform_create(self, serializer):
        """Comment modification."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id', id))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        """Comment request."""
        post_id = self.kwargs.get('post_id', id)
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset
