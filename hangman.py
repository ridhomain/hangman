## Library
import random

## Reading file into list
with open('asset/words.txt') as words:
    word_list = words.read().splitlines()

## Initial data
the_word = random.choice(word_list).lower()
chances = 9
guesses = []
correct_guesses = []
answer = list(set(the_word))

print("Welcome to the Shitty Hangman")
print("   Try to guess the word!")
print("-----------------------------")

## Main Logic 
while chances > 0:
    print(f'Chances left: {chances}')

    ## Print current guess
    word_list = [letter if letter in correct_guesses else '_' for letter in the_word]
    print(' '.join(word_list))
    print("\n")

    guess_letter = input("Guess letter: ").lower()

    if guess_letter in guesses:
        print(f"You already guessed '{guess_letter}'")
    else:
        if guess_letter in the_word:
            correct_guesses.append(guess_letter)
            guesses.append(guess_letter)
            chances -= 1
        else:
            guesses.append(guess_letter)
            chances -= 1
    
    ## Check Win Condition
    if len(correct_guesses) == len(answer):
        print("You win!")
        break
    elif chances == 0:
        print("You lost!")
        

    


