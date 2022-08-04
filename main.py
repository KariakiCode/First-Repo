import random
import numpy as np
from app import words

#get_word
#hangman
# ------ which is the length of the word
#each guess letter have an index in the word so append it in the line index

def get_word():
    word = random.choice(words)
    return word

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def hangman():
    used_letters = []
    guess_word = get_word()
    print(guess_word)
    word_list = list(guess_word)
    guess_line = ['-' for i in range(len(guess_word))]
    new_line = np.array(guess_line)
    print(' '.join(new_line))
    bool = True
    limit = 5
    while bool and limit != 0:
        player = input('Enter a letter  ')
        if len(player) > 1:
            print('invalid input try again: ')
            continue
        else:
            if player not in word_list:
                limit = limit - 1
                print(f'live remaining {limit}')
                if player in used_letters:
                    print('already used that letter')
                    continue
                used_letters.append(player)
                print('used_letters: ', used_letters)
            if player in word_list:
                if player in used_letters:
                    print('already used that letter')
                    continue
                data = guess_word.index(player)
                main_data = list_duplicates_of(guess_word, player)
                new_line[main_data] = player
                print(' '.join(new_line))
            if list(new_line) == word_list:
                bool = False
    if limit == 0:
        print('you did not guess the word')
        playagain()
    print('\n')
    print('you guessed the word:', ''.join(new_line))

def playagain():
    divInput = input('play again? Y/N: ').lower()
    if divInput == 'y':
        hangman()
    elif divInput == 'n':
        quit()

hangman()


