"""One Shot Wordle"""

__author__ = "730553797"

user_word: str = input("What is your 6-letter guess? ")
secret_word = "python"

while len(user_word) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! Try again: ")
    user_word = input()
else:
    if user_word != secret_word:
            print("Not quite. Play again soon!")
    else:
        if user_word == secret_word:
            print("Woo! You got it! ")  


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
result: str = ""

while  i < len(user_word):
    if user_word[i] == secret_word[i]:
        result += GREEN_BOX
    elif user_word[i] in secret_word:
        result += YELLOW_BOX
    else:
        result += WHITE_BOX
    i += 1

print(result)