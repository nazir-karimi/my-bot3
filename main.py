from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("8796614951:AAFLHeXgNkyaZ56UxNvaTMZLS-pJ7sKzXrA")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات روشن شد!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیام شما: " + update.message.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot started...")

app.run_polling()
