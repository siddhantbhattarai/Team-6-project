from rest_framework import serializers
from .models import Post, PostCategory, Comment
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=25)
    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.CharField()
    publishedon = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = PostCategory
        fields = '__all__'
    def create(self, validated_data):
        return PostCategory.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class PostSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('pending', 'Pending Review'),
    ('archive', 'Archive'),
    ('bin', 'Bin'),
    )
    
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    title = serializers.CharField(max_length=255)
    url = serializers.SlugField(max_length=250)
    category = serializers.PrimaryKeyRelatedField(queryset=PostCategory.objects.all())
    body = serializers.CharField()
    featured_img = serializers.ImageField()
    tags = serializers.StringRelatedField(many=True)
    metatitle = serializers.CharField(max_length=255)
    metabody = serializers.CharField(max_length=350)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    publishedon = serializers.DateTimeField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.category = validated_data.get('category', instance.category)
        instance.body = validated_data.get('body', instance.body)
        instance.featured_img = validated_data.get('featured_img', instance.featured_img)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.metatitle = validated_data.get('metatitle', instance.metatitle)
        instance.metabody = validated_data.get('metabody', instance.metabody)
        instance.author = validated_data.get('author', instance.author)
        instance.publishedon = validated_data.get('publishedon', instance.publishedon)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    body = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance