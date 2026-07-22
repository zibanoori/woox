from django.db import models
from ckeditor.fields import RichTextField

class Core(models.Model):
    title = models.CharField(max_length=100, blank=True)
    website_title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="core/", blank=True)
    favicon = models.ImageField(upload_to="core/", blank=True)
    copyright = RichTextField(blank=True)
    
    def __str__(self):
        return "Core Details"