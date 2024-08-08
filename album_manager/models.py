from django.db import models

# Create your models here.

class Artist (models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.name

class Album (models.Model):
    title = models.CharField(max_length=50, null=False)
    release_year = models.IntegerField(null=False)
    genre = models.CharField(max_length=50, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    front_page = models.ImageField(upload_to='front_images')

    def __str__(self) -> str:
        return f"{self.title} - {self.release_year}"