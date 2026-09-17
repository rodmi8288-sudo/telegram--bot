from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# =========================
# توكن البوت
# =========================
TOKEN = "8837641175:AAG06ZQrdVWf3aScyJ02MUt_2D-HzuzUix0"

# =========================
# اسم القناة
# =========================
CHANNEL = "@offresAliexpressDZ2025"


# =========================
# الأزرار
# =========================
def get_keyboard():

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

    return InlineKeyboardMarkup(keyboard)


# =========================
# أمر Start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "مرحبا بك ❤️\n\n"
        "📦 ابعثلي رابط منتج من AliExpress\n"
        "وسأقوم بتحضير العرض ونشره في القناة 🔥",
        reply_markup=get_keyboard()
    )


# =========================
# استقبال الرسائل والروابط
# =========================
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()

    # التأكد من رابط AliExpress
    if "aliexpress.com" not in text.lower():

        await update.message.reply_text(
            "❌ هذا ليس رابط AliExpress.\n\n"
            "📦 ابعثلي رابط المنتج من AliExpress."
        )
        return

    # =========================
    # إنشاء نص العرض
    # =========================
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

        "❤️ لا تفوتي العرض!\n\n"
        "#AliExpress"
    )

    markup = get_keyboard()

    # =========================
    # نشر في القناة
    # =========================
    try:

        await context.bot.send_message(
            chat_id=CHANNEL,
            text=message,
            reply_markup=markup,
            disable_web_page_preview=False
        )

        # =========================
        # الرد على الشخص داخل البوت
        # =========================
        await update.message.reply_text(
            "✅ تم نشر العرض بنجاح في القناة ❤️\n\n"
            + message,
            reply_markup=markup,
            disable_web_page_preview=False
        )

        print("تم نشر العرض بنجاح ✅")

    except Exception as e:

        print("ERROR:", e)

        await update.message.reply_text(
            "❌ ما قدرتش ننشر العرض في القناة.\n\n"
            "تأكدي أن البوت مضاف كمسؤول فيرسائل."
        )


# =========================
# التعامل مع الأزرار
# =========================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "points":

        await query.message.reply_text(
            "⭐ مراجعة وجمع النقاط يوميا ⭐\n\n"
            "يمكنك مراجعة النقاط يوميا والاستفادة من التخفيضات."
        )

    elif query.data == "coins":

        await query.message.reply_text(
            "💸 تخفيض العملات على منتجات السلة 💸\n\n"
            "أرسل رابط منتج AliExpress وسأساعدك في نشر العرض."
        )

    elif query.data == "channel":

        await query.message.reply_text(
            "❤️ اشترك في القناة للمزيد من العروض ❤️\n\n"
            "📢 @offresAliexpressDZ2025"
        )


# =========================
# تشغيل البوت
# =========================
def main():

    print("جاري تشغيل البوت...")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            reply
        )
    )

    app.add_handler(
        CallbackQueryHandler(button)
    )

    print("Bot is running...")

    app.run_polling()


# =========================
# البداية
# =========================
if __name__ == "__main__":
    main()

