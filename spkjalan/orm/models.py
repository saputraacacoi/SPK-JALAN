from django.db import models
from django.contrib.auth.models import User
import time
import os

class Alternatif(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.TextField()
    total = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'alternatif'
        ordering = ['id']