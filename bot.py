import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    CallbackQueryHandler,
)

# Load .env if exists
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable not set. ضع توكن البوت في متغير بيئة BOT_TOKEN أو في ملف .env (انظر README.md)."
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("قول مرحباً", callback_data="hello")],
        [InlineKeyboardButton("معلومات", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"مرحبا {user.first_name or 'صديق'}! أنا بوت تجريبي.\nأرسل رسالة لأتجاوب أو اضغط على الأزرار أدناه.",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - بدء المحادثة\n/help - عرض هذه المساعدة\nأرسل أي رسالة وسيقوم البوت بردها"
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "hello":
        await query.edit_message_text("مرحبًا! كيف يمكنني مساعدتك اليوم؟")
    elif query.data == "about":
        await query.edit_message_text("بوت تجريبي مبني بـ python-telegram-bot.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # مثال بسيط: إذا بدأ المستخدم بـ "/upper " يرد النص بالأحرف الكبيرة
    if text.startswith("/upper "):
        await update.message.reply_text(text[len("/upper ") :].upper())
    else:
        await update.message.reply_text(f"استلمت: {text}")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot started — running with polling. اضغط Ctrl+C للإيقاف.")
    app.run_polling()


if __name__ == "__main__":
    main()