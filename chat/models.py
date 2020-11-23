from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS_CHOICES = [
    ('a', 'Active user'),
    ('b', 'Banned user'),
]


class User(AbstractUser):
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10:-1]
