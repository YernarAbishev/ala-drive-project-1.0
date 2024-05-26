from django.db import models
from datetime import datetime
from tinymce.models import HTMLField



class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="news/images/")
    posted_date = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = HTMLField(null=True, blank=True)
    video_url = models.CharField("Видео (URL)", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title