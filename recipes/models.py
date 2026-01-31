from django.db import models
from django.contrib.auth.models import User


# 🍽️ Recipe Model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()  # related_name='likes'

    def __str__(self):
        return self.title


# 💬 Comment Model
class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"


# ❤️ Like Model
class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.title}"
