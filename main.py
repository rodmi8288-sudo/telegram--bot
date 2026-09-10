from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# حطي هنا التوكن الجديد من BotFather
TOKEN ="8708373953:AAE1dFhswk54tiFWNr-VI3G_4k_w5tPUWRE"

# اسم قناتك
CHANNEL = "@offresAliexpressDZ2025"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ مراجعة وجمع النقاط يوميا ⭐",
                callback_data="points"
            )
        ],
        [
            InlineKeyboardButton(
                "💸 تخفيض العملات على منتجات السلة 💸",
                callback_data="coins"
            )
        ],
        [
            InlineKeyboardButton(
                "❤️ اشترك في القناة للمزيد من العروض ❤️",
                callback_data="channel"
            )
        ],
    ]

    await update.message.reply_text(
        "مرحبا بك ❤️\n\n"
        "ابعثلي رابط منتج من AliExpress "
        "وسأنشره لك في البوت والقناة 🔥",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    if "aliexpress.com" not in text.lower():

        await update.message.reply_text(
            "❌ ابعثلي رابط منتج من AliExpress فقط 📦"
        )
        return

    message = (
        "🔥 عرض جديد من AliExpress 🔥\n\n"
        "💰 عرض بين الأسعار والعملات:\n"
        f"🔗 {text}\n\n"
        "📦 عرض الحزمة:\n"
        f"🔗 {text}\n\n"
        "💎 عرض السوبر:\n"
        f"🔗 {text}\n\n"
        "🔥 عرض محدود:\n"
        f"🔗 {text}\n\n"
        "#AliExpressSaverBot ✅"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ مراجعة وجمع النقاط يوميا ⭐",
                callback_data="points"
            )
        ],
        [
            InlineKeyboardButton(
                "💸 تخفيض العملات على منتجات السلة 💸",
                callback_data="coins"
            )
        ],
        [
            InlineKeyboardButton(
                "❤️ اشترك في القناة للمزيد من العروض ❤️",
                callback_data="channel"
            )
        ],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    try:

        await context.bot.send_message(
            chat_id=CHANNEL,
            text=message,
            reply_markup=markup,
            disable_web_page_preview=False
        )

        await update.message.reply_text(
            message,
            reply_markup=markup,
            disable_web_page_preview=False
        )

        print("تم نشر العرض في البوت والقناة ✅")

    except Exception as e:

        await update.message.reply_text(
            "❌ حدث خطأ أثناء نشر العرض.\n\n"
            "تأكدي أن البوت مسؤول في القناة "
            "وعنده صلاحية نشر الرسائل."
        )

        print("ERROR:", e)


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

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        reply
    )
)

app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")

app.run_polling()
