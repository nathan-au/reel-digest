from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from core.config import REEL_DIGEST_BOT_TOKEN
from pipeline.verification import verify_message, clean_url
from pipeline.pipeline import process_reel
from database.insertion import insert_user, insert_user_reel
from database.selection import select_user_reels
from pipeline.extraction import get_reel_id

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Hello " + user.first_name + ", Welcome to Reel Digest! Share an Instagram Reel with me and I will summarize it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    message_user = update.message.from_user

    insert_user(message_user.id, message_user.first_name)

    if (not verify_message(message_text)):
        await update.message.reply_text("Please share an Instagram Reel.")
        return
    
    clean_reel_url = clean_url(message_text)
    
    reel_summary = process_reel(clean_reel_url)
    if (reel_summary == None):
        await update.message.reply_text("Reel could not be processed. Please try again.")
        return
    
    reel_id = get_reel_id(clean_reel_url)
    if (reel_id != None):
        insert_user_reel(message_user.id, reel_id)
    else:
        print("User_reel could not be saved.")

    await update.message.reply_text(reel_summary)

async def recent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    recent = select_user_reels(user_id)
    if (not recent):
        await update.message.reply_text("You haven't summarized any Reels yet!")
        return
    await update.message.reply_text("Here are your 5 most recent Reel summaries.")

    for summary in recent:
        formatted_message = []
        formatted_message.append(summary[0])
        formatted_message.append(summary[1] + "\n")
        formatted_message.append(summary[2])
        await update.message.reply_text("\n".join(formatted_message))

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here is the list of available commands:\n\n/start - Displays the welcome message\n/help - Displays this list of commands\n/recent - Displays your 5 most recent Reel summaries"
    )

def initialize_bot():
    bot = ApplicationBuilder().token(REEL_DIGEST_BOT_TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("recent", recent))
    bot.add_handler(CommandHandler("help", help))

    bot.add_handler(MessageHandler(filters.ALL, handle_message))
    print("\nReelDigestBot is ONLINE at https://t.me/ReelDigestBot\n")
    bot.run_polling()

if __name__ == "__main__":
    initialize_bot()