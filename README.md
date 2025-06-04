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

### Docker で実行する場合

1. `.env` ファイルを作成し、`DISCORD_TOKEN` などの環境変数を設定します。サンプルとして `.env.example` を用意しています。
2. Docker イメージをビルドし、コンテナを起動します:

```bash
docker compose up -d
```

コンテナが起動すると、5 分ごとに RSS フィードを確認して新しいエントリを Discord チャンネルへ投稿します。
