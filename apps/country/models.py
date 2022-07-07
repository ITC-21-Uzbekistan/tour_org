import uuid
from django.db import models
from apps.gallery.models import Image
from apps.language.models import Language
from utils.abstract import AbstractModel


class Country(AbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_name = models.CharField(max_length=255, null=True, blank=True)
    country_url = models.CharField(max_length=255)
    country_meta_keywords = models.CharField(max_length=500)
    country_images = models.ManyToManyField(Image, db_table='country_images', related_name='country_images')

    class Meta:
        db_table = 'country'
        ordering = ['id']

    def __str__(self):
        return self.country_name


class ContentCountry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=255, null=True, blank=True)
    country_info = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'content_country'
        ordering = ['id']
