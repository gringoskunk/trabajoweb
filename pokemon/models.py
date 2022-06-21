from django.db import models


class pokemon(models.Model):      # Creating model class
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    number = models.IntegerField()

    def __str__(self):
        return self.name
