from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
=======
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()
>>>>>>> 51441947e05d0a2ef62c62bfaef66c1a2a6ca0ae
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
<<<<<<< HEAD
    
=======
>>>>>>> 51441947e05d0a2ef62c62bfaef66c1a2a6ca0ae
