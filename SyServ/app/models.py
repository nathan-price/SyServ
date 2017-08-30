"""
Definition of models.
"""

from django.db import models

# Create your models here.
class gsi(models.Model):
    matchid = models.BigIntegerField(default=0)
    steamid = models.CharField(default="", max_length=32, blank=True)
    steamname = models.CharField(default="", max_length=32, blank=True)
    team = models.CharField(default="", max_length=1, blank=True)
    hp = models.PositiveSmallIntegerField(default=0)
    mana = models.PositiveSmallIntegerField(default=0)
    gpm = models.PositiveSmallIntegerField(default=0)
    xpm = models.PositiveSmallIntegerField(default=0)
    alive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
