# Lyrical Lines

## About the Project
Lyrical Lines is a Django web app that accepts a song (Artist and Title) and provides a summary of each song’s lyrics and a list of any countries mentioned in the song.

## Table of Contents
- [Key Features](#key-features)
- [Installation](#installation)
- [Notes](#notes)

## Key Features
- As an admin, you can add a song by providing the artist's name and song title.
- Once the song has been processed by the app, you can see a summary of the song's lyrics in one sentence (e.g., "This song is about love and growing up").
- You can see a list of countries mentioned in the song (or an empty string if no countries are mentioned).

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/devketanpro/LyricalLines
    ```
2. Make sure you have Docker installed on your machine.
3. Navigate to the project directory:
    ```sh
    cd LyricalLines
    ```
4. Create a `.env` file with your own credentials for now:
    ```sh
    cp sample.env .env
    ```
5. Build the project using Docker Compose:
    ```sh
    make build
    ```
6. Start the server:
    ```sh
    make start
    ```
7. Create a superuser:
    ```sh
    make createsuperuser
    ```
8. Enter the Django shell:
    ```sh
    make shell
    ```
9. Stop the containers:
    ```sh
    make down
    ```
10. Open your web browser and visit: [http://localhost:8000](http://localhost:8000)


## Notes
- Musixmatch only provides a part of the lyrics.
- Uses OpenAI GPT API for summarizing lyrics and getting a list of countries.
