import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import CommandHandler

from random import randint

from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_request import FilmRequest
from kinopoisk_unofficial.request.films.box_office_request import BoxOfficeRequest
import kinopoisk_unofficial.client.exception.not_found

from kinopoisk.movie import Movie

api_client = KinopoiskApiClient("92281495-5e0b-445d-bb8f-9d7b55c77525")
bot = telegram.Bot(token='5354662458:AAEVEhmBwoZIji8S6jVt_JjkgO7hnKihcEc')

reply_keyboard = [['/find_random_movie']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def tg_start(update, context):
    update.message.reply_text("Приветствую тебя! Напиши мне название фильма/мультфильма/сериала"
                              " и я найду их для тебя. Либо я могу подобрать для тебя рандомную картину, надеюсь"
                              " тебе понравится !", reply_markup=markup)


def tg_help(update, context):
    update.message.reply_text("Я не умею помогать.")


def close_keyboard(update, context):
    update.message.reply_text("Хорошо!", reply_markup=ReplyKeyboardRemove())


def find_random_movie(update, context):
    check = True
    while (check == True):
        try:
            movie_id = randint(298, 1450000)
            request = FilmRequest(movie_id)
            request2 = BoxOfficeRequest(movie_id)
            response = api_client.films.send_film_request(request)
            response2 = api_client.films.send_box_office_request(request2)
            movie_info(update, response, response2, movie_id)
            check = False
        except kinopoisk_unofficial.client.exception.not_found.NotFound:
            print("Пустой ID, ищу дальше...")


def find_list_movie(update, context):
    movie_list = Movie.objects.search(update.message.text)
    button_list = []
    for i in range(0, len(movie_list)):
        button_list.append(InlineKeyboardButton(movie_list[i].title, callback_data=movie_list[i].id))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    update.message.reply_text("Найденные фильмы: ", reply_markup=reply_markup)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def find_name_movie(update, context):
    query = update.callback_query
    variant = query.data
    query.answer()
    try:
        request = FilmRequest(variant)
        request2 = BoxOfficeRequest(variant)
        response = api_client.films.send_film_request(request)
        response2 = api_client.films.send_box_office_request(request2)
        movie_info(query, response, response2, variant)
    except kinopoisk_unofficial.client.exception.not_found.NotFound:
        query.message.reply_text("Это не фильм/мультфильм/сериал. Выберите что-нибудь другое.")



def movie_info(update, response, response2, movie_id):
    print(response.film)
    print(response2.items)

    if response.film.year == None:
        year = "Неизвестно"
    else:
        year = str(response.film.year)


    if response.film.name_ru == None and response.film.name_en == None:
        update.message.reply_text(response.film.name_original + ' (' + year + ')')
    elif response.film.name_ru == None:
        update.message.reply_text(response.film.name_en + ' (' + year + ')')
    elif response.film.name_en == None:
        update.message.reply_text(response.film.name_ru + ' (' + year + ')')

    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=response.film.poster_url)

    final_budget = "Неизвестно"
    for i in range(0, len(response2.items)):
        budget = str(response2.items[i])
        if budget[16: budget.find('amount=') - 3:] == "BUDGET":
            final_budget = budget[budget.find("amount=") + 7: budget.find("currency_code=") - 2] + ' ' + budget[budget.find("symbol=") + 8: budget.rfind("'")]
            break

    final_world = "Неизвестно"
    for i in range(0, len(response2.items)):
        world = str(response2.items[i])
        if world[16: world.find('amount=') - 3:] == "WORLD":
            final_world = world[world.find("amount=") + 7: world.find("currency_code=") - 2] + ' ' +  world[world.find("symbol=") + 8: world.rfind("'")]
            break

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
    else:
        age = "Неизвестно"

    if response.film.film_length == None:
        film_length = "Неизвестно"
    else:
        film_length = str(response.film.film_length) + " мин."

    if response.film.description == None:
        description = "Отсутствует"
    else:
        description = response.film.description

    if response.film.rating_kinopoisk == None:
        rating_kinopoisk = "Отсутствует"
    else:
        rating_kinopoisk = str(response.film.rating_kinopoisk)

    print(year)
    print(country_final)
    print(genre_final)
    print(final_budget)
    print(final_world)
    print(age)
    print(film_length)
    print(description)
    print(rating_kinopoisk)

    update.message.reply_text('Год производства: ' + year + '\nСтрана: ' + country_final
                              + '\nЖанр: ' + genre_final
                              + '\nБюджет: ' + final_budget
                              + '\nСборы в мире: ' + final_world
                              + '\nВозраст: ' + age
                              + '\nВремя: ' + film_length
                              + '\n\nОбзор: ' + description
                              + '\n\nРейтинг фильма: ' + rating_kinopoisk)

    bot.send_message(chat_id, '[Посмотреть фильм можно здесь](https://www.kinopoisk.ru/film/' + str(movie_id) + '/)',
                     parse_mode='Markdown')


def main():
    updater = Updater('5354662458:AAEVEhmBwoZIji8S6jVt_JjkgO7hnKihcEc', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("help", tg_help))
    dp.add_handler(CommandHandler("close_keyboard", close_keyboard))

    dp.add_handler(CommandHandler("find_random_movie", find_random_movie))
    dp.add_handler(CommandHandler("find_list_movie", find_list_movie))

    dp.add_handler(CallbackQueryHandler(find_name_movie))
    dp.add_handler(MessageHandler(Filters.text, find_list_movie))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()