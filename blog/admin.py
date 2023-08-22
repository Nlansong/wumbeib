from django.contrib import admin
from .models import Tag, PostModel

# Register your models here.
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = [
        'title',
        'author',
        'date_created',
    ]
    
    
    prepopulated_fields = {
        'slug':('title',)
    }
    
admin.site.register(PostModel, PostAdmin)