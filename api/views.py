from .models import Post, Company, User, Apply
from .serializer import PostSerializer

# django rest api
from rest_framework import viewsets
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    # ModelViewSet의 경우 커스텀이 까다로울듯 -> 일반 ViewSet이나 generic 이용
    queryset = Post.objects.all()
    serializer_class = PostSerializer
