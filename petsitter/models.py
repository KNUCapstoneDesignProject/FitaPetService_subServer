from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    thumnail = models.TextField()
    uploadedFile = models.FileField(upload_to="Uploaded Files/")
    fileSize = models.FloatField()
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

class ImgDocument(models.Model):
    title = models.CharField(max_length=200)
    uploadedImg = models.ImageField(upload_to="Pet Images/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    userId = models.EmailField(max_length=20)
    lat = models.FloatField()
    long = models.FloatField()
