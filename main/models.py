from time import time
from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    
    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
        .filter(status='published')



class Post(models.Model):
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, help_text="Title of your Post.")
    slug = models.SlugField(max_length=250 , unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "blog/%Y/%m/%d",db_index=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
         ordering = ('-publish',)
    # def clean(self):
    #     self.body = self.body.replace("\r", "\n")
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('main:post_detail',
        args=[self.publish.year,
        self.publish.month,self.publish.day, self.slug])