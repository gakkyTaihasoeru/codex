# Discord RSS Bot

This repository contains a simple Discord bot that posts updates from an RSS feed into a channel.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

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

4. Run the bot:

```bash
python rss_bot.py
```

The bot will check the RSS feed every five minutes and send new entries to the specified channel.
