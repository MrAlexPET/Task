import telebot
import random

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    lives = 10

    word_variants = ['футбол', 'кот', 'хомяк', 'салон', 'школа']

    word_right = random.choice(word_variants)

    word_in_game = "_" * len(word_right)

    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Хай! Если хочешь сыграть, напиши /play')
    elif message.text == "/play":
        bot.send_message(message.from_user.id,
                         'Количество жизней:' + str(lives) + '\n' + 'Слово' + str(word_in_game) + '\n' + 'Введи букву:')
        bot.register_next_step_handler(message, get_letter, lives, word_in_game, word_right)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_letter(message, lives, word_in_game, word_right):
    try:
        if (len(message.text) == 1) and (message.text.islower()):
            letter = message.text
            swat = 0
            if letter in word_right:
                index = -1
                swat = 1
                while word_in_game.count(letter) != word_right.count(letter):
                    index = word_right.find(letter, index + 1)
                    word_in_game = word_in_game[:index:] + letter + word_in_game[(index + 1):]
                    message1 = bot.send_message(message.from_user.id, 'Ты угадал! Эта буква есть в слове.' + '\n' +
                                                'Количество жизней:' + str(lives) + '\n' + word_in_game)
            else:
                lives = lives - 1
                swat = 2
                message2 = bot.send_message(message.from_user.id, 'Неверная буква :(' + '\n' + 'Количество жизней:' +
                                            str(lives) + '\n' + word_in_game)
        else:
            swat = 3
            message3 = bot.send_message(message.from_user.id, 'Пожалуйста введите только одну строчную букву')
        if ('_' in word_in_game) and (lives > 0):
            bot.send_message(message.from_user.id, 'Введи букву:')
            if swat == 1:
                message10 = message1
            elif swat == 2:
                message10 = message2
            elif swat == 3:
                message10 = message3
            bot.register_next_step_handler(message10, get_letter, lives, word_in_game, word_right)
        elif lives > 0:
            bot.send_message(message.from_user.id, 'Ты победил! Что бы начать новую игру, напиши /play')
        else:
            bot.send_message(message.from_user.id, 'Правильное слово: ' + word_right + '\n' + 'Game Over' +
                             '\n' + 'Что бы начать новую игру, напиши /play')

    except:
        bot.send_message(message.from_user.id, 'Пожалуйста введите только одну строчную букву')


bot.polling()