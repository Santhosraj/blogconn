from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime
from django.http import JsonResponse

# Create your models here.
User = get_user_model()


# class Post(models.Model):
#     user = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='post_images')
#     caption = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now)
#     no_of_likes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.user


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    about = models.TextField(blank=True)
    interest = models.TextField(blank=True)


    profile_image = models.ImageField(upload_to="profile_images/", default='profile.png')

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Uploads', on_delete=models.CASCADE, null=True)
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    date_added = models.DateTimeField(default=datetime.now(), blank=True)
    content = models.CharField(max_length=1000)

    def __str__(self):
       return f"{self.user} on {self.post}"

class Uploads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    body = models.TextField()
    comments = models.ManyToManyField(Comment, blank=True)
    no_of_likes = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts')


    def __str__(self):
        return self.title + '|' + str(self.user)


class Room(models.Model):
    name = models.CharField(max_length=10000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

