"""
Definition of models.
"""

from datetime import datetime
from enum import unique
from tabnanny import verbose
from django.urls import reverse
from django.contrib import admin
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = 'posted', verbose_name = 'Заголовок')
    description = models.TextField(verbose_name = 'Краткое содержание')
    content = models.TextField(verbose_name = 'Полное содержание')
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Опубликована')
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default= 'temp.jpg', verbose_name='Путь к картинке')

    def get_absolute_url(self):
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Posts'
        ordering = ['-posted']
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = 'Текст комментария')
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата комментария')  # Опубликовано - posted
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор комментария')
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = 'Статья комментария')

    def __str__(self):
        return self.author
    
    class Meta:
        db_table = 'Comment'
        ordering = ['-date'] # posted
        verbose_name = 'Комментарии к статье блога'
        verbose_name_plural = 'Комментарии к статьям блога'

admin.site.register(Comment)