import uuid

from django.db import models

from apps.language.models import Language
from utils.abstract import AbstractModel


class Image(AbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'image'
        ordering = ['id']


class ContentImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, related_name='image_content')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    alt_text = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        db_table = 'content_image'
        ordering = ['id']