from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
import config

import yt_dlp

def download_reel(url):
    ydl_opts = {"outtmpl": "bucket/%(id)s.%(ext)s"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Downloaded.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        "Hello " + user.first_name + " and welcome to Reel Digest! Send me an Instagram reel link and I will summarize it for you."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text

    if "instagram.com" not in message_text:
        await update.message.reply_text("Please share an Instagram reel.")
    else:
        print("\nReceived: " + message_text)
        download_reel(message_text)
        await update.message.reply_text("Instagram reel received successfully.")

app = ApplicationBuilder().token(config.REEL_DIGEST_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_message))
print("\nReelDigestBot is online at http://t.me/ReelDigestBot")
app.run_polling()