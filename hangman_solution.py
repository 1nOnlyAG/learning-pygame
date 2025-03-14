correct_word = "faucet"
guessed = []
correct = 0
incorrect = 0
num_of_errors = 6
while correct != len(set(correct_word)) and incorrect < num_of_errors:
    a = input("enter a letter... ")[0]
    if a in guessed:
        print("already guessed that")
        continue

    guessed.append(a)
    if a in correct_word:
        correct += 1
    else:
        incorrect += 1
        print(str(num_of_errors - incorrect) + " incorrect guesses left")


    for letter in correct_word:
        if letter in guessed:
            print(letter, end="")
        else:
            print("*", end="")
    print()
if correct == len(set(correct_word)):
    print("You won in " + str(len(guessed)) + " guesses")
else:
    print("You lost with " + str(incorrect) + " incorrect guesses")