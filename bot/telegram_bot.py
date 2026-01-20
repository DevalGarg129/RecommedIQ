import sys, os, asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.search import search_and_predict
from backend.app import get_next_recommendation
from config.config import TELEGRAM_BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome!! Type /learn to get learning material")

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    material = get_next_recommendation(user_id)
    await update.message.reply_text(f"Today's Material:\n{material}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    result, predicted = search_and_predict(query)
    await asyncio.sleep(0.5)
    if result:
        msg = f"Result:\n{result['topic']}\nLink: {result['link']}"
    
    if predicted:
        msg += f"\n\nNext Suggested Topic:\n{predicted}"
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Topic not found! Try another or use /learn.")
        


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("learn", learn))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Bot started successfully. Waiting for Telegram commands...")
    app.run_polling()

if __name__ == "__main__":
    main()
