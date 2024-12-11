from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Replace these with your bot token and personal Telegram ID
BOT_TOKEN = "8105675182:AAFImrHEjl1Hk1r2Cxjv9nfPVyJ-wN-72Lg"
ADMIN_CHAT_ID = "928448167"

def forward_message(update: Update, context: CallbackContext) -> None:
    # Forward user messages to your admin account
    context.bot.send_message(chat_id=ADMIN_CHAT_ID,
                             text=f"Message from @{update.effective_user.username}:\n\n{update.message.text}")

def reply_to_user(update: Update, context: CallbackContext) -> None:
    # Reply back to the user when you reply to forwarded messages
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.text.split("Message from @")[1].split(":")[0]
        context.bot.send_message(chat_id=user_id, text=update.message.text)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handle incoming messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
