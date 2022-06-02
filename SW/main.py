from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import telegram
import requests
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_request import FilmRequest
from kinopoisk_unofficial.request.films.box_office_request import BoxOfficeRequest
from kinopoisk_unofficial.request.films.film_video_request import FilmVideoRequest
from kinopoisk_unofficial.request.films.seasons_request import SeasonsRequest
from kinopoisk_unofficial.request.films.facts_request import FactsRequest
from kinopoisk_unofficial.request.films.search_by_keyword_request import SearchByKeywordRequest

api_client = KinopoiskApiClient("92281495-5e0b-445d-bb8f-9d7b55c77525")
bot = telegram.Bot(token='5354662458:AAEVEhmBwoZIji8S6jVt_JjkgO7hnKihcEc')


reply_keyboard = [['/find_name_movie', '/find_genre_movie'], ['/find_random_movie']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def tg_start(update, context):
    update.message.reply_text("Приветствую тебя! Напиши мне название фильма или мультфильма"
                              " и я найду их для тебя. Либо я могу подобрать для тебя рандомную картину, надеюсь"
                              " тебе понравится !", reply_markup=markup)

def tg_help(update, context):
    update.message.reply_text("Я не умею помогать.")

def close_keyboard(update, context):
    update.message.reply_text("Хорошо!", reply_markup=ReplyKeyboardRemove())


def find_name_movie(update, context):
    movie_id = 298
    request = FilmRequest(movie_id)
    request2 = BoxOfficeRequest(movie_id)
    movie_info(update, request, request2, movie_id)


def movie_info(update, request, request2, movie_id):
    response = api_client.films.send_film_request(request)
    response2 = api_client.films.send_box_office_request(request2)

    print(response.film)
    print(response2.items)

    update.message.reply_text(response.film.name_ru + ' (' + str(response.film.year) + ')')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=response.film.poster_url)

    final_budget = ""
    budget_symbol = ""
    for i in range(0, len(response2.items)):
        budget = str(response2.items[i])
        if budget[16: budget.find('amount=') - 3:] == "BUDGET":
            final_budget = budget[budget.find("amount=") + 7: budget.find("currency_code=") - 2]
            budget_symbol = budget[budget.find("symbol=") + 8: budget.rfind("'")]
            break
        else:
            final_budget = "Неизвестно"
            budget_symbol = ""

    final_world = ""
    world_symbol = ""
    for i in range(0, len(response2.items)):
        world = str(response2.items[i])
        if world[16: world.find('amount=') - 3:] == "WORLD":
            final_world = world[world.find("amount=") + 7: world.find("currency_code=") - 2]
            world_symbol = world[world.find("symbol=") + 8: world.rfind("'")]
            break
        else:
            final_world = "Неизвестно"
            world_symbol = ""

    genre_final = ""
    for i in range(0, len(response.film.genres)):
        genre = str(response.film.genres[i])
        if i == len(response.film.genres) - 1:
            genre_final += genre[genre.find("'") + 1: genre.rfind("'")]
        else:
            genre_final += genre[genre.find("'") + 1: genre.rfind("'")] + ', '

    country_final = ""
    for i in range(0, len(response.film.countries)):
        country = str(response.film.countries[i])
        if i == len(response.film.countries) - 1:
            country_final += country[country.find("'") + 1: country.rfind("'")]
        else:
            country_final += country[country.find("'") + 1: country.rfind("'")] + ', '

    age = ""
    if response.film.rating_age_limits == "age6":
        age = "6+"
    elif response.film.rating_age_limits == "age3":
        age = "3+"
    elif response.film.rating_age_limits == "age0":
        age = "0+"
    elif response.film.rating_age_limits == "age12":
        age = "12+"
    elif response.film.rating_age_limits == "age18":
        age = "18+"
    elif response.film.rating_age_limits == "age16":
        age = "16+"

    update.message.reply_text('Год производства: ' + str(response.film.year) + '\nСтрана: ' + country_final
                              + '\nЖанр: ' + genre_final
                              + '\nБюджет: ' + final_budget + ' ' + budget_symbol
                              + '\nСборы в мире: ' + final_world + ' ' + world_symbol
                              + '\nВозраст: ' + age
                              + '\nВремя: ' + str(response.film.film_length) + " мин."
                              + '\n\nОбзор: ' + response.film.description
                              + '\n\nРейтинг фильма: ' + str(response.film.rating_kinopoisk))

    bot.send_message(chat_id, '[Посмотреть фильм можно здесь](https://www.kinopoisk.ru/film/' + str(movie_id) + '/)',
                     parse_mode='Markdown')


def main():
    updater = Updater('5354662458:AAEVEhmBwoZIji8S6jVt_JjkgO7hnKihcEc', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("help", tg_help))
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("find_name_movie", find_name_movie))

    movie_handler = MessageHandler(Filters.text, find_name_movie)
    dp.add_handler(movie_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()