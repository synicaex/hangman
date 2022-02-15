import random
from numpy import char

word_list = ["problem","schule"]
word = random.choice(word_list)
print(word)
guesses =""

while True:
    guess = input("Geben sie einen Buchstaben ein: ")
    if len(guess) > 1:
        print("Einen Buchstaben oder das gesamte Wort eigeben!")
    guesses += guess
    for char in word:
        if char in guesses:
            print(char,)
        else:
            print("_")
    if guesses == word:
        print("Du hast das wort erraten!")
        break
    else:
        continue