import asyncio

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

TOKEN ="8892522284:AAEtpfIZ5OYkNm8HxJjtOldVJkwNPE8w9ig"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⭐ مراجعة وجمع النقاط يوميا ⭐", callback_data="points")],
        [InlineKeyboardButton("💸 تخفيض العملات على منتجات السلة 💸", callback_data="coins")],
        [InlineKeyboardButton("❤️ اشترك في القناة للمزيد من العروض ❤️", callback_data="channel")],
    ]

    await update.message.reply_text(
        "مرحبا بك ❤️\n"
        "ابعثلي رابط منتج من AliExpress وسأعرض لك العروض المتاحة 🔥",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "aliexpress.com" not in text:
        await update.message.reply_text(
            "ابعثلي رابط منتج من AliExpress فقط 📦"
        )
        return

    message = (
        "🔥 لقيت هذا المنتج في AliExpress\n\n"
        "💰 عرض بين الأسعار والعملات:\n"
        f"🔗 الرابط: {text}\n\n"
        "📦 عرض الحزمة:\n"
        f"🔗 الرابط: {text}\n\n"
        "💎 عرض السوبر:\n"
        f"🔗 الرابط: {text}\n\n"
        "🔥 عرض محدود:\n"
        f"🔗 الرابط: {text}\n\n"
        "#AliExpressSaverBot ✅"
    )

    keyboard = [
        [InlineKeyboardButton("⭐ مراجعة وجمع النقاط يوميا ⭐", callback_data="points")],
        [InlineKeyboardButton("💸 تخفيض العملات على منتجات السلة 💸", callback_data="coins")],
        [InlineKeyboardButton("❤️ اشترك في القناة للمزيد من العروض ❤️", callback_data="channel")],
    ]

    await update.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=False
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "points":
        await query.message.reply_text(
            "⭐ صفحة مراجعة وجمع النقاط يوميا"
        )

    elif query.data == "coins":
        await query.message.reply_text(
            "💸 تخفيض العملات على منتجات السلة"
        )

    elif query.data == "channel":
        await query.message.reply_text(
            "❤️ اشترك في القناة للمزيد من العروض"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")

asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
