import random

lives = 10

word_variants = ['dog', 'cat', 'hamster']

word_right = random.choice(word_variants)

word_in_game = '_' * len(word_right)

while ('_' in word_in_game) and (lives > 0):
    print('Lives count:', lives)
    print(word_in_game)
    letter = input('Guess letter:')

    if letter in word_right:
        print('You are right! We have this letter in word.')
        index = -1

        while word_in_game.count(letter) != word_right.count(letter):
            index = word_right.find(letter, index + 1)
            word_in_game = word_in_game[:index:] + letter + word_in_game[(index + 1):]

    else:
        lives -= 1
        print('Try again :(')
    print('*' * 10)

if lives > 0:
    print(word_right)
    print('You win!')
else:
    print('Right word: ', word_right)
    print('Game over.')


