from django.db import models

class core(models.Model):
    title = models.charField(max_length=100, blank=True)
    website_title = models.charField(max_length=100, blank=True)

