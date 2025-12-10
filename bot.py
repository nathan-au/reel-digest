from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
import config
from summarization import summarize_reel
from extraction import download_reel, convert_reel_to_audio, convert_audio_to_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Hello " + user.first_name + ", welcome to Reel Digest! Share an Instagram reel with me and I will summarize it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text

    if ("instagram.com" not in message_text):
        await update.message.reply_text("Please share an Instagram reel.")
    else:
        clean_url = message_text.split("?")[0]
        print("\nReceived: " + clean_url)
        if (download_reel(clean_url) and convert_reel_to_audio()):
            reel_text = convert_audio_to_text()
            if (reel_text != False):
                response = summarize_reel()
                print("\r[3/4] Generating summary...", end = "", flush = True)
                print("\r[4/4] Process completed.    ")
                await update.message.reply_text(response)
            else:
                print("Reel could not be processed.\n")
                await update.message.reply_text("Instagram reel could not be processed.")

        else:
            print("Reel could not be processed.\n")
            await update.message.reply_text("Instagram reel could not be processed.")

def initialize_bot():
    bot = ApplicationBuilder().token(config.REEL_DIGEST_BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.ALL, handle_message))
    print("\nReelDigestBot is online at https://t.me/ReelDigestBot")
    bot.run_polling()

initialize_bot()