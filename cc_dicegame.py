import random

high_score = 0
roll_dice = "Roll Dice"
end_game = "End Game"

print(f"Current High Score: {high_score}")


def dice_game():
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    print(f"You roll a...{result1}")
    print(f"You roll a...{result2}")
    global high_score
    high_score = result1 + result2
    print(f"You rolled a total of: {high_score}")
    if high_score > 0:
        print("New high score!\n")


while True:
    print(f" 1) {roll_dice}\n  2) {end_game}")
    choice = input("Enter your choice: ")

    if choice == "1":
        dice_game()
    elif choice == "2":
        print("Leave Game")
        break
