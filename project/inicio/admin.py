from django.contrib import admin
from .models import UserProfile, BlogEntry

admin.site.register(UserProfile)
admin.site.register(BlogEntry)