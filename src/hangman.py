import random 
import string
from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0 :
        
        print('you have ', lives ,' lives left and you have used this letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for  letter in word]
        print('current word: ' , ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1 
                print('Letter is noit in word')
        elif user_letter in used_letters:
            print('You have already use this character. Please try again!')

        else:
            print('Invalid character. Please try again.')

    if lives == 0 :
        print('you died. sorry, the word was ', word)
    print('you guessed the word', word , '!!')


hangman()