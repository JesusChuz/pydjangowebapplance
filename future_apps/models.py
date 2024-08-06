from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)
    profile_pic =  models.ImageField(null=True, blank=True, upload_to='images/profile/')
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    meta_url = models.URLField(max_length=255, blank=True, null=True)
    pinterest_url = models.URLField(max_length=255, blank=True, null=True)
    soundcloud_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)    
    is_premium = models.BooleanField(default=False)  

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return self.user.username



class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    shoe_image = models.ImageField(null=False, blank=False, upload_to='images/')
    body = models.TextField(null=True, blank=True, max_length=255)
    post_date = models.DateField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # ForeignKey to Brand
    # brand = models.CharField(max_length=255, default='select_shoe')  # Revert back to CharField
    likes = models.ManyToManyField(User, related_name='blog_post')    
    colaboration = models.CharField(null=True, blank=True, max_length=255)
    color_scheme_1 = models.CharField(max_length=255)
    color_scheme_2 = models.CharField(max_length=255)
    color_scheme_3 = models.CharField(max_length=255)
    model = models.CharField(max_length=255)


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

