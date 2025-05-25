# 🤖 PatchyBot – LoL & TFT Patch Notes Discord Bot

**PatchyBot** is a Discord bot that fetches and posts the latest **League of Legends** and **Teamfight Tactics** patch notes directly in your server’s chat.  
Just use a simple `!patch` or `!patch tft` command and get official updates instantly — no links or browsers required.

---

## 🚀 What It Does

- 📰 Fetches the latest **LoL** or **TFT** patch notes via web scraping
- 🧾 Extracts title, description, image, and link from the official Riot site
- 💬 Displays patch info in a clean, embedded Discord message
- 🆘 Includes a help command and friendly fallback for unrecognized input

---

## 🔍 Features

- 💡 `!patch` → Gets League of Legends patch notes
- 💡 `!patch tft` → Gets Teamfight Tactics patch notes
- 🧠 Auto-formats embeds with images and patch summaries
- ✅ Zero setup needed for users in Discord (just invite and use)
- 🛠 Built with `discord.py`, `BeautifulSoup`, and `requests`

---

## 🖼 Output Example

Here’s what PatchyBot looks like in action inside a Discord server:

![alt text](https://github.com/Jessecomo/PatchyBot-LoL-Patch-Notes-Discord-Bot/blob/main/Patchybot-Example.png)

---

## 🔐 API Key Setup (.env Required)

This project uses an `.env` file to store your **Discord API key** securely.  
You must create your own `.env` file in the root of the project:
TOKEN=your-discord-bot-token-here

