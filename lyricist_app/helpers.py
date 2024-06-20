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
        return data["message"]["body"]["lyrics"]["lyrics_body"].split("*******")[0]
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Timeout as timeout_err:
        logger.error(f"Request timed out: {timeout_err}")
    except RequestException as req_err:
        logger.error(f"Request exception: {req_err}")
    except Exception as err:
        logger.error(f"An error occurred: {err}")

    return None  # Return None if there was an error


def get_summary_and_country_from_openai(lyrics):
    """
    Fetches summary and countries mentioned in song lyrics using OpenAI API.

    Args:
    - lyrics (str): The song lyrics for which summary and countries should be extracted.

    Returns:
    - tuple or None: A tuple containing (summary, countries) extracted from the lyrics.
                     Returns None if there's an error during API request or processing.
    """

    openai_url = settings.OPENAI_URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
    }

    # Define the components of the prompt for OpenAI
    prompt_components = """
        Task: "Create a dictionary containing two objects: 'summary' and 'countries'."
        Context: "You will be given song lyrics. The 'summary' should encapsulate the lyrics in one sentence, "
                "and 'countries' should list any countries mentioned in the lyrics."
        Exemplars:  "Example: Given the lyrics provided, the output should be: "
                    '{"summary": "The lyrics describe the economic hardships and struggles faced by tradesmen, soldiers, and sailors in old England, with a hope for better times to come.", "countries": ["England"]}.'

        Persona: "You are an expert in natural language processing and text summarization."
        Format: "Return the output as a dictionary with the 'summary' and 'countries' keys."
        Tone: "The tone should be concise and informative."
    """

    # Construct the data payload
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": prompt_components},
            {"role": "user", "content": lyrics},
        ],
    }

    try:
        response = requests.post(openai_url, headers=headers, json=data)
        response.raise_for_status()
        data = response.json()
        response_data = json.loads(data["choices"][0]["message"]["content"])
        return response_data.get("summary"), response_data.get("summary")
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Timeout as timeout_err:
        logger.error(f"Request timed out: {timeout_err}")
    except RequestException as req_err:
        logger.error(f"Request exception: {req_err}")
    except Exception as err:
        logger.error(f"An error occurred: {err}")

    return None, None
