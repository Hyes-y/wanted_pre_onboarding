# django rest api
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# local modules
from .models import Post
from .serializer import PostSerializer, PostDetailSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    채용 공고 관련 API
    """
    queryset = Post.objects.select_related('company').all()
    serializer_class = PostSerializer
    # 검색 기능
    filter_backends = [SearchFilter]
    search_fields = ['position', 'skill', 'description']

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        if self.action == "list":
            return PostSerializer

        return PostDetailSerializer

