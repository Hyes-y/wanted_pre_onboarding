from .models import Post
from rest_framework import serializers

# Serializers define the API representation.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('reg_date', 'update_date', 'id')
