from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model

class Blog(models.Model):
    titulo = models.CharField(max_length=60)
    contenido = models.TextField(max_length=2000)
class UserProfile(AbstractUser):
    avatar = models.FileField(upload_to='files/avatars', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.username}'


class BlogEntry(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Titulo = models.TextField()
    Subtitulo = models.TextField()
    Texto = models.TextField()
    Imagen = models.ImageField(upload_to='files/blog_images', blank=True, null=True)
    likes = models.ManyToManyField(UserProfile, related_name='blog_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.Titulo[:50]}"

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username} at {self.timestamp}"