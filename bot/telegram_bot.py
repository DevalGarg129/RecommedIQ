import sys, os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.app import get_next_recommendation
from config.config import TELEGRAM_BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome!! Type /learn to get learning material")


async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    material = get_next_recommendation(user_id)
    await update.message.reply_text(f"Today's Material:\n{material}")


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("learn", learn))

    print("Bot started successfully. Waiting for Telegram commands...")
    app.run_polling()

if __name__ == "__main__":
    main()
