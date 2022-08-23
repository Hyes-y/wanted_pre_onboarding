from django.urls import include, path
from . import views

# django rest framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]