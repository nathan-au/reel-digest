from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
import config
from verification import verify_message, clean_url
from process import process_reel
from database import insert_user, insert_user_reel, select_user_reels
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Hello " + user.first_name + ", welcome to Reel Digest! Share an Instagram reel with me and I will summarize it for you.")

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    history = select_user_reels(user_id)
    await update.message.reply_text(str(history))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    message_user = update.message.from_user

    insert_user(message_user.id, message_user.first_name)

    if (not verify_message(message_text)):
        await update.message.reply_text("Please share an Instagram Reel.")
        return
    
    clean_reel_url = clean_url(message_text)
    
    if (not process_reel(clean_reel_url)):
        await update.message.reply_text("Instagram Reel could not be processed.")
        return
    
    with open("bucket/info.json", "r") as f:
        info = json.load(f)

    insert_user_reel(message_user.id, info.get("id"))

    with open("bucket/summary.txt", "r") as f:
        reel_summary = f.read()
    await update.message.reply_text(reel_summary)


def initialize_bot():
    bot = ApplicationBuilder().token(config.REEL_DIGEST_BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("history", history))

    bot.add_handler(MessageHandler(filters.ALL, handle_message))
    print("\nReelDigestBot is online at https://t.me/ReelDigestBot")
    bot.run_polling()