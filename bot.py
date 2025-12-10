from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
import config
from extraction import extract_reel

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Hello " + user.first_name + ", welcome to Reel Digest! Share an Instagram reel with me and I will summarize it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text

    if ("instagram.com" not in message_text):
        await update.message.reply_text("Please share an Instagram reel.")
    else:
        if (extract_reel(message_text)):
            await update.message.reply_text("Instagram reel extracted successfully.")
        else:
            await update.message.reply_text("Instagram reel could not be extracted.")

def initialize_bot():
    bot = ApplicationBuilder().token(config.REEL_DIGEST_BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.ALL, handle_message))
    print("\nReelDigestBot is ONLINE: https://t.me/ReelDigestBot\n")
    bot.run_polling()