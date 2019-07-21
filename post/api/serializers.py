from rest_framework import serializers
from post.models import Post
class PostSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
   )
   username = serializers.SerializerMethodField()
   class Meta:
       model = Post
       fields = [
           'username',
           'title',
           'content',
           'image',
           'url',
           'created',
           'modified_by'
       ]

   def get_username(self, obj):
        return str(obj.user.username)

class PostUpdateCreateSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = [
           'title',
           'content',
           'image',
       ]
