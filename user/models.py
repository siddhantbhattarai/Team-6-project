from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to="media/uploads/profile/", blank=True)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    
    #for social links
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    
    
    
    def __str__(self):
        return self.user.username