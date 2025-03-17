import telebot
import requests
import os
from yt_dlp import YoutubeDL

# Telegram Bot Token from BotFather
BOT_TOKEN = xyz
bot = telebot.TeleBot(BOT_TOKEN)

def download_instagram_reel(url):
    options = {
        'format': 'best',
        'outtmpl': 'reel.mp4'
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])
    return 'reel.mp4'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Send me an Instagram Reels link, and I'll download it for you!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if 'instagram.com/reel' in url:
        bot.send_message(message.chat.id, "Downloading the reel, please wait...")
        try:
            video_path = download_instagram_reel(url)
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video)
            os.remove(video_path)  # Delete after sending
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {str(e)}")
    else:
        bot.send_message(message.chat.id, "Please send a valid Instagram Reels link!")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)
