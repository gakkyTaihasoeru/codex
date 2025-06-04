# Discord RSS Bot

This repository contains a simple Discord bot that posts updates from an RSS feed into a channel.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Docker (optional if using the container setup)

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a Discord bot and invite it to your server. Obtain the bot token and the channel ID where you want the RSS updates posted.

3. Set the following environment variables:

- `DISCORD_TOKEN` – your bot token
- `CHANNEL_ID` – the ID of the channel to post in
- `RSS_FEED_URL` – the RSS feed URL to monitor

4. Run the bot locally:

```bash
python rss_bot.py
```

### Running with Docker

1. Create a `.env` file and set environment variables such as `DISCORD_TOKEN`. See `.env.example` for a template.
2. Build the Docker image and start the container:

```bash
docker compose up -d
```

Once running, the container checks the RSS feed every five minutes and posts new entries to the Discord channel.
