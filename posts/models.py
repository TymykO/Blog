from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.author} - {self.title}'