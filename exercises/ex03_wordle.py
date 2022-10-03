"""Wordle with turns."""

__author__ = "730553797"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Checking if a character is at the index."""
    assert len(character) == 1
    i: int = 0
    while i < len(word):
        if character == word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifying known characters."""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(guess, secret[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(number: int) -> str:
    """Makes sure guess is right amount of characters."""
    guess: str = input("Enter a " + str(number) + " character word: ")
    while len(guess) != number:
        guess = input("That wasn't " + str(number) + " chars! Try again: ")
    else:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 0
    secret: str = "codes"
    stop: bool = False
    while not stop:
        n += 1 
        print(f"=== Turn {n}/6 ===")
        guess = input_guess(5)
        print(guess)
        print(emojified(guess, secret))
        if guess == secret:
            stop = True
        elif n > 5:
            stop = True
    if guess == secret:
        print(f"You won in {n}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()