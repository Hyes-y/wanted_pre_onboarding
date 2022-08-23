# django rest api
from rest_framework import viewsets

# local modules
from .models import Post
from .serializer import PostSerializer, PostDetailSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    채용 공고 관련 API
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        if self.action == "list":
            return PostSerializer

        return PostDetailSerializer

