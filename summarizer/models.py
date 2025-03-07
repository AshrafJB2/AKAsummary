from django.db import models
from django.contrib.auth.models import User

# Create your models here.

VALUE_CHOICES = (
        (1, 'Short'),
        (2, 'Medium'),
        (3, 'Long'),
    )

class Summarization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    summary = models.TextField()
    keywords = models.JSONField()
    depth = models.PositiveSmallIntegerField(choices=VALUE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
