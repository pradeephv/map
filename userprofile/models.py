from django.db import models


class Profile(models.Model):
    image = models.FileField()




class Obstacle(models.Model):
    where = models.CharField(max_length=255)
    source_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)

    def __str__(self):
        return self.where

        