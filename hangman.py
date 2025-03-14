
correct_word = "faucets"

guessed = [2]
def has_been_guessed(letter):
    return letter in guessed

def print_redacted_word():
    for i in range(0, len(correct_word)):
        # if the letter we are on has been guessed
        # then we print the letter unredacted
        # else we print *
        # if has_been_guessed(correct_word[i]):
        if correct_word[i] in guessed:
            print(correct_word[i], end="")
        else:
            print("*", end="")
    print()

limit_guesses = 9
while False:
    guess = input("please enter a letter... ")
    # guessed = guessed + [guess]
    guessed.append(guess)
    print_redacted_word()

    # if we have guessed all the letters in correct_word
    number_correct = 0
    # for i in range(0, len(correct_word)):
    #     if correct_word[]
    # if :
    #     print("you won")
    #     break

    # if len(guessed) is over limit_guesses we break loop
    if len(guessed) > limit_guesses:
        print("you lost")
        break
