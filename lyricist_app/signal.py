from django.db.models.signals import post_save
from django.dispatch import receiver

from lyricist_app.helpers import (
    fetch_lyrics_from_musixmatch,
    get_summary_and_country_from_openai,
)
from lyricist_app.models import Country, Song


@receiver(post_save, sender=Song)
def update_song_details_from_api(sender, instance, created, **kwargs):
    """
    Signal receiver function triggered after saving a Song instance.
    Fetches lyrics from an external API using Musixmatch, then retrieves
    summary and countries mentioned using OpenAI API. Updates the Song instance
    with fetched lyrics, summary, and associated countries.
    """

    if created:
        fetched_lyrics = str(fetch_lyrics_from_musixmatch(instance.artist, instance.title))
        summary, countries = get_summary_and_country_from_openai(fetched_lyrics)
        if countries:
            for country in countries:
                c, _ = Country.objects.get_or_create(name=country)
                instance.countries.add(c)
        instance.lyrics = fetched_lyrics
        instance.summary = summary
        instance.save()
