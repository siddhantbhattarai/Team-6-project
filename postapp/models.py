from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField #CK editor Rich text field
# Create your models here.
class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=25, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    description = models.TextField()
    publishedon = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Categories"


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('pending', 'Pending Review'),
    ('archive', 'Archive'),
    ('bin', 'Bin'),
    )

    id = models.AutoField(primary_key=True)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')

    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey('PostCategory',on_delete=models.CASCADE)
    body = RichTextUploadingField()
    featured_img = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    tags = TaggableManager()

    metatitle = models.CharField(max_length=255)
    metabody = models.CharField(max_length=350)

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    publishedon = models.DateTimeField(editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ('-publishedon',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.url])
    
    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)
    
    
    

    
    


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=50)
    email=models.EmailField()
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)