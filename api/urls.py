from django.urls import include, path
from . import views

# django rest framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]