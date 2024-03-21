from django.db import models


# Create your models here.

class AiResponse(models.Model):
    query = models.CharField(max_length=200)
    ai_response = models.TextField(max_length=200)
    def __str__(self):
        return self.query
