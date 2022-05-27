from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import KeyboardButton

reply_keyboard = [['/find_name_movie', '/find_genre_movie'], ['/find_random_movie']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
reply_keyboard2 = [['/find_rating_movie']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)


def tg_start(update, context):
    update.message.reply_text("Привет! Я КиноБот! Что я могу:", reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text("Хорошо!", reply_markup=ReplyKeyboardRemove()
    )


def tg_help(update, context):
    update.message.reply_text("Я пока не умею помогать.")


def find_name_movie(update, context):
    update.message.reply_text('Фильм', reply_markup=markup2)


def main():
    updater = Updater('5354662458:AAEVEhmBwoZIji8S6jVt_JjkgO7hnKihcEc', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("help", tg_help))
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("find_name_movie", find_name_movie))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()