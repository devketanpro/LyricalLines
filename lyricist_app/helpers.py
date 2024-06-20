import json
import logging
import requests

from django.conf import settings
from requests.exceptions import HTTPError, Timeout, RequestException

logger = logging.getLogger(__name__)

def fetch_lyrics_from_musixmatch(artist, title):
    """
    Fetch lyrics from Musixmatch API for a given artist and title.

    Args:
        artist (str): The name of the artist.
        title (str): The title of the song.

    Returns:
        str: The lyrics of the song if found.
        None: If there was an error during the request or lyrics are not found.
    """

    musicmatch_url = settings.MUSIXMATCH_URL
    params = {
        "q_track": title,
        "q_artist": artist,
        "apikey": settings.MUSIXMATCH_API_KEY,
    }
    try:
        response = requests.get(musicmatch_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['message']['body']['lyrics']['lyrics_body'].split("*******")[0]
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Timeout as timeout_err:
        logger.error(f"Request timed out: {timeout_err}")
    except RequestException as req_err:
        logger.error(f"Request exception: {req_err}")
    except Exception as err:
        logger.error(f"An error occurred: {err}")

    return None  # Return None if there was an error
