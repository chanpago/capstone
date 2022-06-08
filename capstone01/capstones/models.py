from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Document(models.Model):
    uploadedFile = models.FileField(upload_to="pipeimages/")
    dateTimeOfUpload =models.DateTimeField(auto_now=True)
