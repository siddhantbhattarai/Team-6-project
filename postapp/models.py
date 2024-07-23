from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

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
    body = models.TextField()
    tags = TaggableManager()

    metatitle = models.CharField(max_length=255)
    metabody = models.CharField(max_length=350)

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    publishedon = models.DateTimeField(editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "News Post"
        ordering = ('-publishedon',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("editpost", args={str(self.id)})