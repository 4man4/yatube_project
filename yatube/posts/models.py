from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Класс групп постов."""
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        """Функция печати имени группы"""
        return self.title


class Post(models.Model):
    """Класс постов."""
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
