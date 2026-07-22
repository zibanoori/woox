from django.db import models

class core(models.Model):
    title = models.charFieldharField(max_length=100, blank=True)
    website_title = models.CharField(max_length=100, blank=True)
    logo = models.ImageFiel(upload_to="core/" ,blank=True)

