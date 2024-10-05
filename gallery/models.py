from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class ArtWork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    created_at = models.DateField()
