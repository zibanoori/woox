from django.db import models

class core(models.Model):
    title = models.CharField(max_length=100, blank=True)
    website_title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="core/", blank=True)
    copyright = models.TextField(blank=True)
    
    def __str__(self):
        return "Core Details"