from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment
from post.models import Post


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created',]

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','id','email')


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','slug','id')

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]