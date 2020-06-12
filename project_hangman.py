import random


def play_game():
    words = ["python", "java", "kotlin", "javascript"]
    random_word = random.choice(words)
    blank_word = list("-" * len(random_word))
    used_letters = set()
    count = 0
    while count < 8:
        print()
        for i in blank_word:
            print(i, end="")
        if list(random_word) == blank_word:
            print("\nYou guessed the word!")
            print("You survived!")
            break
        letter = input("\nInput a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in random_word and letter not in blank_word:
            for i, j in enumerate(random_word):
                if j == letter:
                    blank_word[i] = j
                    used_letters.add(letter)
        else:
            if letter in used_letters:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                count += 1
                used_letters.add(letter)
    else:
        print("You are hanged!")


print("H A N G M A N")
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit:')
    if user_choice == "play":
        play_game()
    elif user_choice == "exit":
        break
