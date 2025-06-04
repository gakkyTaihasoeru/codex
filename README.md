<p align="right"><a href="README.en.md">English</a></p>

# Discord RSS Bot

このリポジトリには、RSSフィードから取得した更新をDiscordのチャンネルに投稿するシンプルなボットが含まれています。

## 必要条件

- Python 3.8以上
- `requirements.txt` に記載された依存関係
- Docker（コンテナ環境を使用する場合は任意）

## セットアップ

1. 依存関係をインストールします:

```bash
pip install -r requirements.txt
```

2. Discordボットを作成し、サーバーに招待します。ボットのトークンとRSSを投稿するチャンネルIDを取得します。

3. 以下の環境変数を設定します:

- `DISCORD_TOKEN` – ボットのトークン
- `CHANNEL_ID` – 投稿先チャンネルのID
- `RSS_FEED_URL` – 監視するRSSフィードのURL

4. ボットをローカルで実行します:

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
