from django.db import models

# Create your models here.
class songmodel(models.Model):
    songname = models.CharField(max_length=100)
    songurl = models.CharField(max_length=100)
    
    def __str__(self):
        return self.songname