import os
import asyncio
import feedparser
import discord

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', '0'))
RSS_FEED_URL = os.getenv('RSS_FEED_URL')

if not all([TOKEN, CHANNEL_ID, RSS_FEED_URL]):
    raise RuntimeError('DISCORD_TOKEN, CHANNEL_ID and RSS_FEED_URL must be set as environment variables')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_published = None

async def poll_feed():
    global last_published
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Could not find channel with ID {CHANNEL_ID}")
        return
    while not client.is_closed():
        feed = feedparser.parse(RSS_FEED_URL)
        for entry in reversed(feed.entries):
            published = entry.get('published_parsed')
            if not published:
                continue
            if last_published is None or published > last_published:
                link = entry.get('link')
                title = entry.get('title')
                await channel.send(f"{title}\n{link}")
                last_published = published
        await asyncio.sleep(300)  # check every 5 minutes

@client.event
def on_ready():
    print(f'Logged in as {client.user}')

client.loop.create_task(poll_feed())
client.run(TOKEN)
