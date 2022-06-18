from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Заголовок',max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField('Дата публикации',auto_created=True,auto_now=True)
    photo = models.ImageField('Прикрепить файл',upload_to='img/%Y-%m-%d/',blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField('Текст комментария',max_length=500)
    photo = models.ImageField('Прикрепить файл', upload_to='img/%Y-%m-%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)