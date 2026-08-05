from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8892522284:AAEtpfIZ5OYkNm8HxJjtOldVJkwNPE8w9ig"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك، البوت يعمل بنجاح!")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "aliexpress.com" in text or "a.aliexpress.com" in text:
        await update.message.reply_text(
            f"""🔥 تم استلام رابط AliExpress

الرابط:
{text}

شكراً، سأعالج الرابط قريباً."""
        )
    else:
        await update.message.reply_text("شكراً على رسالتك، سأرد عليك قريباً.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot is running...")
app.run_polling()