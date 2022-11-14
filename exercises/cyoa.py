"""Pokemon text battle!"""

from random import randint

__author__ = "730553797"


GREEN_SEEDLING: str = "\U0001F331"
EXCLAMATION_MARK: str = "\U0000203C"
WATER: str = "\U0001F4A7"
FIRE: str = "\U0001F525"
RUSTLE: str = "\U0001F343"
POW: str = "\U0001F4A5"
HEART: str = "\U00002764"

# index:
# 0 = name
# 1 = health
starters = {
    1: ["Charmander", 39], 
    2: ["Squirtle", 44],
    3: ["Bulbasaur", 45]
}

mobs = {
    1: ["Bulbasaur", 45],
    2: ["Diglet", 30]
}

# index:
# 0 = attack move
# 1 = damage value
attacks = {
    1: ["Bite", randint(1, 5)],
    2: ["Tackle", randint(1, 6)],
    3: ["Watergun", randint(1, 8)],
    4: ["Flamethrower", randint(1, 10)]
}


points: int = 0
player: str = ""


def greet() -> None:
    """Greets the player."""
    global player
    greeting: str = "Welcome to Pokemon Text Battle! This will be based off of the original Pokemon where the goal is to battle and defeat your rival! Along the way, points will be given out according to your actions. For the purpose of this game, please type all choices in lowercase!"
    print("\n")
    print(greeting)
    print("\n")
    player = input("What is your trainer name? ")
    print("\n")
    print(f"Happy adventures {player}! ")


def count_points(x: int) -> int:
    """Function to assign points."""
    x += 100
    total_points: str = (f"===Total Points: {x}===")
    print("+100")
    print(total_points)
    return (x)


def choice(x: list) -> str:
    """Makes sure a valid choice is chosen."""
    valid: bool = False
    option: str = ""
    while not valid:
        option = input("Please enter a response: ")
        print("\n")
        for i in range(len(x)):
            if option == x[i]:
                valid = True
        if not valid:
            print("That is not a valid option.")
            print("\n")
    y: str = f"You have chosen {option}"
    print(y)
    return option


def sleep() -> None:
    """If choice sleep is made."""
    print("You walk back home because you are too tired to go adventuring.")
    print("\n")
    print(f"{EXCLAMATION_MARK} A wild Bulbasaur appears {EXCLAMATION_MARK}")
    print("\n")
    print(f"{GREEN_SEEDLING} Bulbasur casts Sleep Powder on {player} {GREEN_SEEDLING}")
    print("\n")
    print(f"{player} begins to feel drowsy")
    print("\n")
    print(f"Sweet dreams {player}!")


def game_over() -> None:
    """Game over function."""
    print("=== GAME OVER ===")
    print(f"Total Points: {points}")
    print("\n")
    print("Thank you for playing!")


def forest() -> None:
    """If player chooses forest route."""
    print(f"{player} ventures off into the nearby forest and befriends a wild Charmander!")
    print("\n")
    print(f"With {player}'s new friend, they go further into the forest where they hear a rustle.")
    print("\n")
    print(f".{RUSTLE}")
    print(f"..{RUSTLE}{RUSTLE}")
    print(f"...{RUSTLE}{RUSTLE}{RUSTLE}")
    print("\n")
    print(f"{EXCLAMATION_MARK} A wild Diglet appears {EXCLAMATION_MARK}")


def battle(personal: str, opponent: str, hp1: int, hp2: int) -> bool:
    """Battle loop."""
    stop: bool = False
    n = 0
    while not stop:
        n += 1
        randomizer: int = randint(0, 4)
        if n % 2 == 0:
            print(f"=== Turn {n} ===")
            print(f"{personal} HP: {HEART}{hp1}")
            print(f"{opponent} HP: {HEART}{hp2}")
            if randomizer == 0:
                print(f"{opponent} attacks {personal} but misses {EXCLAMATION_MARK}")
            elif randomizer == 1: 
                print(f"{opponent} uses {POW}{attacks[1][0]}{EXCLAMATION_MARK}{POW}")
                print(f"{opponent} attacks {personal} for {attacks[1][1]} damage {EXCLAMATION_MARK}")
                hp1 = hp1 - attacks[1][1]
            elif randomizer == 2:
                print(f"{opponent} uses {POW}{attacks[2][0]}{EXCLAMATION_MARK}{POW}")
                print(f"{opponent} attacks {personal} for {attacks[2][1]} damage {EXCLAMATION_MARK}")
                hp1 = hp1 - attacks[2][1]
            elif randomizer == 3:
                print(f"{opponent} uses {WATER}{attacks[3][0]}{EXCLAMATION_MARK}{WATER}")
                print(f"{opponent} attacks {personal} for {attacks[3][1]} damage {EXCLAMATION_MARK}")
                hp1 = hp1 - attacks[3][1]
            elif randomizer == 4:
                print(f"{opponent} uses {FIRE}{attacks[4][0]}{EXCLAMATION_MARK}{FIRE}")
                print(f"{opponent} attacks {personal} for {attacks[4][1]} damage {EXCLAMATION_MARK}")
                hp1 = hp1 - attacks[4][1]
        else:
            print(f"=== Turn {n} ===")
            print("\n")
            print(f"{personal} HP: {HEART}{hp1}")
            print(f"{opponent} HP: {HEART}{hp2}")
            print("\n")
            print("Please type 1, 2, 3, or 4")
            print("1. Bite")
            print("2. Tackle")
            print("3. Watergun")
            print("4. Flamethrower")
            print("\n")
            userMove: int = int(input("Choose a move..."))
            print("\n")

            while userMove < 1 or userMove > 4:    
                print("Please input a valid response")
                print("\n")
                print("Please type 1, 2, 3, or 4")
                print("1. Bite")
                print("2. Tackle")
                print("3. Watergun")
                print("4. Flamethrower")
                print("\n")
                userMove: int = int(input("Choose a move..."))
                print("\n")

            if userMove == 1: 
                print(f"{personal} uses {POW}{attacks[1][0]}{EXCLAMATION_MARK}{POW}")
                print(f"{personal} attacks {opponent} for {attacks[1][1]} damage {EXCLAMATION_MARK}")
                hp2 = hp2 - attacks[1][1]
            elif userMove == 2:
                print(f"{personal} uses {POW}{attacks[2][0]}{EXCLAMATION_MARK}{POW}")
                print(f"{personal} attacks {opponent} for {attacks[2][1]} damage {EXCLAMATION_MARK}")
                hp2 = hp2 - attacks[2][1]
            elif userMove == 3:
                print(f"{personal} uses {WATER}{attacks[3][0]}{EXCLAMATION_MARK}{WATER}")
                print(f"{personal} attacks {opponent} for {attacks[3][1]} damage {EXCLAMATION_MARK}")
                hp2 = hp2 - attacks[3][1]
            elif userMove == 4:
                print(f"{personal} uses {FIRE}{attacks[4][0]}{EXCLAMATION_MARK}{FIRE}")
                print(f"{personal} attacks {opponent} for {attacks[4][1]} damage {EXCLAMATION_MARK}")
                hp2 = hp2 - attacks[4][1]

        if hp1 <= 0:
            stop = True
            print("\n")
            print("You have been defeated, try again next time.")
            return False
        if hp2 <= 0:
            stop = True
            print("\n")
            print(f"Congratulations! {opponent} has been defeated {EXCLAMATION_MARK}")
            return True
    

def town() -> None:
    """If player chooses town route."""
    print(f"{player} ventures into the nearby town and befriends a wild Squirtle!")
    print("\n")
    print(f"As {player} is about to leave town, {player}'s Rival is looking for a fight!")
    print("\n")
    print(f"{player} has no choice but to fight{EXCLAMATION_MARK}")
    print("\n")
    print("Rival throws out their pokemon")
    print("\n")
    print(f"{EXCLAMATION_MARK} Bulbasuar appears {EXCLAMATION_MARK}")


def main() -> None:
    """Entrypoint of the game and game loop."""
    greet()
    global points
    print("\n")
    print(f"{player}'s journey begins as they leaves their home. {player} has the choices of: Sleep, Forest, Town, or Quit ")
    print("\n")

    options: list = ["sleep", "forest", "town", "quit"]
    x: str = ""
    x = choice(options)

    if x == options[0]:
        points = count_points(points)
        print("\n")
        sleep()
        game_over()
    elif x == options[1]:
        points = count_points(points)
        print("\n")
        forest()
        winner = battle(starters[1][0], mobs[2][0], starters[1][1], mobs[2][1])
        if winner:
            points = points + 300
            print("+300")
        print("\n")
        game_over()

    elif x == options[2]:
        points = count_points(points)
        print("\n")
        town()
        winner = battle(starters[2][0], mobs[1][0], starters[2][1], mobs[1][1])
        if winner:
            points = points + 500
            print("+500")
        print("\n")
        game_over()

    elif x == options[3]:
        game_over()    
    

if __name__ == "__main__":
    main()