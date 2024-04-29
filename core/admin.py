from django.contrib import admin
from .models import ( 
    BlogCategory, Blog, BlogFile, Question,
    Report, Member, MediaCategory, Media
)
# Register your models here.


admin.site.register(BlogCategory)

admin.site.register(Blog)

admin.site.register(BlogFile)

admin.site.register(Question)

admin.site.register(Report)

admin.site.register(Member)

admin.site.register(MediaCategory)

admin.site.register(Media)