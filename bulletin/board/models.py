from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    CATEGORY = [
        ("tanks", "Танки"),
        ("khila", "Хилы"),
        ("dd", "ДД"),
        ("merchants", "Торговцы"),
        ("guildmasters", "Гилдмастеры"),
        ("questgivers", "Квестгиверы"),
        ("blacksmiths", "Кузнецы"),
        ("tanners", "Кожевники",),
        ("potions_makers", "Зельевары"),
        ("spell_masters", "Мастера заклинаний")
    ]
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=128, unique=True)
    post_category = models.CharField(max_length=16, choices=CATEGORY,
                                     default="dd")
    post_text = RichTextUploadingField(config_name="custom")  # Uploading
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.post_author} : {self.post_title} : "
                f"{self.post_category}")

    def get_absolute_url(self):
        return f'/posts/{self.pk}'


class Reply(models.Model):
    reply_author = models.OneToOneField(User, on_delete=models.CASCADE)
    reply_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    reply_text = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
