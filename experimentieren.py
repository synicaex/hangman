import random
from numpy import char

word_list = ["problem","schule"]
word = random.choice(word_list)
print(word)
guesses =""

while True:
    guess = input("Geben sie einen Buchstaben ein: ")
    if guess == word:
        print("Du hast das Wort erraten!")
        break
    else:
        if len(guess) > 1:
            print("Einen Buchstaben oder das gesamte Wort eigeben!")    
        else:
            guesses += guess
            yeah = True
            for char in word:
                if char in guesses:
                    print(char, end = '', flush=True)
                else:
                    print('_', end = '', flush=True)
                    yeah = False
                print()
            if yeah:
                print("Super!")
                break

        