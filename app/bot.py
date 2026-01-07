from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from core.config import REEL_DIGEST_BOT_TOKEN
from jobs.inspector import is_valid_platform, extract_url, is_reel
from jobs.processor import process_reel
from data.insert import insert_user, insert_user_reel
from data.select import select_recent
from jobs.investigator import get_reel_id

# COMMANDS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text("Hello " + user.first_name + ", Welcome to Reel Digest! Share an Instagram Reel, YouTube Short, or TikTok video with me and I will summarize it for you.")

async def recent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    message_id = update.message.id

    recent = select_recent(user_id)
    if (not recent):
        await update.message.reply_text("You haven't summarized any Reels yet!")
        return
    await update.message.reply_text("Here are your 5 most recent video summaries.", reply_to_message_id = message_id
)

    for summary in recent:
        formatted_message = []
        formatted_message.append(summary[0])
        formatted_message.append(summary[1] + "\n")
        formatted_message.append(summary[2])
        await update.message.reply_text("\n".join(formatted_message))

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here is the list of available commands:\n\n/start - Displays the welcome message\n/help - Displays this list of commands\n/recent - Displays your 5 most recent summaries"
    )

# MESSAGES

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    message_id = update.message.id

    if (not message_text):
        await update.message.reply_text("Please share an Instagram Reel, YouTube Short, or Tiktok video.", reply_to_message_id = message_id)
        return
    
    message_user = update.message.from_user

    if (not is_valid_platform(message_text)):
        await update.message.reply_text("Please share an Instagram Reel, YouTube Short, or Tiktok video.", reply_to_message_id = message_id)
        return
    
    reel_url = extract_url(message_text)

    if (not is_reel(reel_url)):
        await update.message.reply_text("Please share an Instagram Reel, YouTube Short, or Tiktok video.", reply_to_message_id = message_id)
        return

    insert_user(message_user.id, message_user.first_name)
    
    reel_summary = process_reel(reel_url)
    if (reel_summary == None):
        await update.message.reply_text("Video could not be processed. Please try again later.", reply_to_message_id = message_id)
        return
    
    reel_id = get_reel_id(reel_url)
    if (reel_id != None):
        insert_user_reel(message_user.id, reel_id)
    else:
        print("User_reel could not be saved.")

    await update.message.reply_text(reel_summary, reply_to_message_id = message_id)

def initialize_bot():
    bot = ApplicationBuilder().token(REEL_DIGEST_BOT_TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("recent", recent))
    bot.add_handler(CommandHandler("help", help))
    bot.add_handler(MessageHandler(filters.ALL, handle_message))

    print("ReelDigestBot is ONLINE at https://t.me/ReelDigestBot")
    bot.run_polling()