from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا بك في غابة الصيد حيث تكون أنت الفريسة")

def main():
    # ضع توكن البوت هنا أو في متغير بيئة TELEGRAM_BOT_TOKEN
    token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running... (Ctrl+C to stop)")
    app.run_polling()

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
