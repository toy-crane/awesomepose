from django.db import models
from django.conf import settings


class Post(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL
            )

    image = models.ImageField()
    content = models.TextField()

    update_at = models.DateTimeField(
            auto_now_add=True,
            )
    create_at = models.DateTimeField(
            auto_now=True,
            )