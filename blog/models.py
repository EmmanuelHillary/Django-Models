from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    published_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

