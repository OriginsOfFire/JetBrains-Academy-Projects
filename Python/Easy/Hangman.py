import random

words = ['python', 'java', 'kotlin', 'javascript']
game_modes = ['play', 'exit']
tries = []
alphabet = list("abcdefghijklomnpqrstuvwxyz")
attempts = 8

print("H A N G M A N\n")
while True:
    word = list(random.choice(words))
    hidden = list("-" * len(word))
    tries = []
    attempts = 8

    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision not in game_modes:
        continue
    elif decision == "exit":
        break
    else:
        while attempts:
            print(''.join(hidden))
            answer = input("Input a letter: ")

            if len(answer) > 1 or answer == "":
                print("You should input a single letter\n")
                continue

            if not answer in alphabet:
                print("Please enter a lowercase English letter\n")
                continue

            if answer in tries:
                print("You've already guessed this letter\n")
                continue
            else:
                tries.append(answer)

            if answer in word and not answer in hidden:
                for i in range(len(word)):
                    if word[i] == answer:
                        hidden[i] = word[i]
                if not hidden.count("-"):
                    print("\nThe word is: " + ''.join(hidden))
                    print("You guessed the word!")
                    print("You survived!\n")
                    break
            else:
                attempts -= 1
                print("That letter doesn't appear in the word")

            if attempts:
                print()
            else:
                print("You lost!\n")