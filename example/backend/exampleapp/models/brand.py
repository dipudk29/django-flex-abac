from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=3000, default="", blank=True)

    class Meta:
        app_label = 'exampleapp'