import random
from words_stages import stages,words

def guess_word():
    word=random.choice(words)
    return word.upper()


def play(word):
    word_completion = '_'*len(word)
    guessed = False
    guessed_word = []
    guessed_letters = []
    tries = 6
    print(f'Lets play :\n {show_hangman(tries)}\n{word_completion}\n')
    while not guessed and tries > 0:
        guess=input("Enter your guess : (letter or word)\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('you already guessed the letter', guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('good job, lets guess another one :)')
                guessed_letters.append(guess)
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_completion = ''.join(word_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print('you already guessed the word', guess)
            elif guess != word:
                print(guess, 'is not the word')
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess')
        print(f'{show_hangman(tries)}\n{word_completion}\n')
    if guessed:
        print('Congrats, you guessed the word ! You win!')
    else:
        print('you are a loser hahaha :D')


def show_hangman(tries):
    return stages[tries]


def main():
    word = guess_word()
    play(word)
    while input('Play again? (Y/N)').upper() == 'Y' : 
        word = guess_word()
        play(word)
if __name__ == '__main__':
    main()
