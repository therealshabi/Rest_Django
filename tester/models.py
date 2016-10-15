from __future__ import unicode_literals

from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Details'
