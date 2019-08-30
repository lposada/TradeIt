from django.db import models

class Snippets(models.Model):
    name = models.CharField(max_length=100)
    