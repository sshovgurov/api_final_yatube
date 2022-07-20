from rest_framework import viewsets, filters

from posts.models import Follow, Comment, Group, Post
from .serializers import PostSerializer, FollowSerializer, CommentSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = self.request.get['post_id']
        queryset = Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()