

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re

# ========== حط التوكن الجديد هنا ==========
TOKEN = "8837641175:AAG06ZQrdVWf3aScyJ02MUt_2D-HzuzUix0"
CHANNEL = "@offresAliexpressDZ2025"
# =========================================

def get_keyboard(link):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 اطلب الآن", url=link)],
        [InlineKeyboardButton("📢 قناتنا", url="https://t.me/offresAliexpressDZ2025")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا ❤️ ابعثلي رابط AliExpress")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.strip()
    if "aliexpress.com" not in text.lower():
        await update.message.reply_text("❌ هذا ليس رابط AliExpress\nابعثلي رابط منتج صحيح")
        return

    m = re.search(r'/item/(\d+)', text)
    pid = m.group(1) if m else "0"
    aff = f"https://s.click.aliexpress.com/e/_{pid}"

    msg = f"🔥 عرض جديد 🔥\n\n{aff}\n\n#Aliexpress_DZ"

    await context.bot.send_message(chat_id=CHANNEL, text=msg, reply_markup=get_keyboard(aff))
    await update.message.reply_text(f"✅ تم النشر في {CHANNEL}\n{aff}")

def main():
    print("جاري تشغيل البوت...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
