import random
def dice_game():
    dice_one = random.randrange(1,6)
    dice_two = random.randrange(1,6)
    result = dice_one + dice_two
    if result == 6 or 7 or 8:
        return "Win"
    else:
        return "Lose"
def main():
    input("Press enter to roll:")
    print(dice_game())
main()