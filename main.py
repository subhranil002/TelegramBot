import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


def start(update, context):
    update.message.reply_text("Hello! ... I'm Subhranil's Bot!")


def contact(update, context):
    update.message.reply_text(
        """
        Linkedin - https://www.linkedin.com/in/subhranilchakraborty/
gitHub - https://github.com/subhranil002
Facebook - https://www.facebook.com/TheSubhranilChakraborty/
Instagram - https://www.instagram.com/subhranil.chakraborty/

I Hope This Helps :)
        """
    )


def helps(update, context):
    update.message.reply_text(
        """
        Hi there! Here are some activities we can do :)

Please follow the commands -

/start - to start conversation
/contact - contact details of Subhranil
/help - to get this menu

I Hope This Helps :)
        """
    )


def handle_message(update, context):
    update.message.reply_text(f'You said "{update.message.text}"')


updator = telegram.ext.Updater(TOKEN, use_context=True)
dispatch = updator.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler("start", start))
dispatch.add_handler(telegram.ext.CommandHandler("contact", contact))
dispatch.add_handler(telegram.ext.CommandHandler("help", helps))
dispatch.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))

updator.start_polling()
updator.idle()
