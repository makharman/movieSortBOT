import telebot
from telebot import types


BOT_TOKEN = '6797367742:AAFfPf6ws-WKtBxEsJOr1p3JPe9G_FyOpYs'

bot = telebot.TeleBot(BOT_TOKEN)

movie_data = {
    "комедия": ["Игрушки", "Поездка в Америку", "Форрест Гамп", "1+1", "Полицейская академия"],
    "драма": ["Зеленая миля", "Потомки", "Клетка", "Престиж", "Проклятый остров"],
    "ужасы": ["Астрал", "Крик", "Оно", "Тихое место", "Оскар"],
    "мульты": ["Шрек", "Немо", "Зверополис", "Хиро", "Тоторо"],

}


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Я бот с топ-5 фильмами по жанрам. Используй команду /top, чтобы увидеть список жанров.')

@bot.message_handler(commands=['top'])
def handle_top(message):
    genres = list(movie_data.keys())
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(genre) for genre in genres])
    bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    genre = message.text.lower()
    if genre in movie_data:
        movies = movie_data[genre]
        response = f"Топ-5 фильмов по жанру '{genre.capitalize()}':\n"
        for idx, movie in enumerate(movies[:5], start=1):
            response += f"{idx}. {movie}\n"
        bot.reply_to(message, response)


bot.polling()
