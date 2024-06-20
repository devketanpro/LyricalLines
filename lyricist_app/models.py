from django.db import models

# Create your models here.


class Country(models.Model):
    """
    Represents a country.

    Attributes:
        name (str): The name of the country.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    """
    Represents a song.

    Attributes:
        artist (str): The name of the artist.
        title (str): The title of the song.
        summary (str): A one-sentence summary of the song's lyrics.
        lyrics (str): The full lyrics of the song.
        countries (ManyToManyField): A list of countries associated with the song.
    """

    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return f"{self.artist} - {self.title}"
