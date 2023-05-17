from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self) :
        return self.title