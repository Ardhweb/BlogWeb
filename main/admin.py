from django.contrib import admin

# Register your models here.
from .models import Topic ,Post



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']