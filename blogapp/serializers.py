from rest_framework import serializers
from .models import Post,Category,Comment
from django.contrib.auth import get_user_model # 추가

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username',]


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.ReadOnlyField(source = 'post.headline')
    class Meta:
        model = Category
        fields = ['posts',]

class PostBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['headline','content','category']

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):# meta도 상속받아주어야한다.
        exclude = ['content', ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'
