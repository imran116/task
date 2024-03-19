from django.db import models


# Create your models here.

class Recipe(models.Model):
    query = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
