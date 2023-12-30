from django.db import models

# Create your models here.

class UploadedSelfie(models.Model):
    selfie = models.ImageField(upload_to='selfies/')


    def __str__(self):
        return self.selfie.name



class Images(models.Model):
    image = models.ImageField(upload_to='images/')
