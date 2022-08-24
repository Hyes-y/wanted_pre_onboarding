from .models import Post, Company
from rest_framework import serializers
import uuid


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('reg_date', 'update_date', 'uid')

    def create(self, validated_data):
        while True:
            uid = str(uuid.uuid4())[:8]
            is_duplicated = self.Meta.model.objects.filter(uid=uid).count()
            if is_duplicated == 0:
                break
        return self.Meta.model.objects.create(uid=uid, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    company_country = serializers.SerializerMethodField()
    company_location = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.name

    def get_company_country(self, obj):
        return obj.company.country

    def get_company_location(self, obj):
        return obj.company.location

    class Meta:
        model = Post
        fields = ('id', 'uid', 'position', 'reward', 'skill',
                  'company_name', 'company_country', 'company_location'
                  )
        read_only_fields = ['uid']


class PostDetailSerializer(PostSerializer):
    related = serializers.SerializerMethodField()

    def get_related(self, obj):
        return Post.objects.filter(company=obj.company).exclude(id=obj.id).values_list('id', 'uid')

    class Meta:
        model = Post
        fields = ('id', 'uid', 'position', 'reward', 'skill', 'description',
                  'company_name', 'company_country', 'company_location',
                  'related'
                  )
        read_only_fields = ['id', 'uid']





