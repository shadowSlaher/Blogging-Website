from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    header_image = models.ImageField(null = True, blank= True, upload_to="images/")
    likes = models.ManyToManyField(User, related_name='blog_post')
    snippet = models.TextField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):     
        return reverse("home")
        # return reverse("article_detail", args=(str(self.id)))
    # kwargs={"pk": self.pk}
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank= True, upload_to='images/profile')
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):     
        return reverse("home")
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    

    
  

    
    

