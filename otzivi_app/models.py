from django.db import models

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.username} - {self.date}'