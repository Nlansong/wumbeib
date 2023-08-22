from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=30, unique=True)
#     slug = models.SlugField()
#     description = models.CharField(max_length=160)
    
#     def __str__(self):
#         return self.title
    
    # class Meta:
    #     unique_together = ('slug', 'parent',)
    #     verbose_name_plural = "Categories"
        

class Tag(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class PostModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    sub_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=160)
    body = models.TextField()
    tag = models.ManyToManyField(Tag, default='')
    #category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='Post')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Posts'
    
    
    
