import random


def create_random_combination(possible_colors, length):
    random_combination = []
    for i in range(0, length):
        random_combination.append(random.choice(possible_colors))
    return random_combination


def evaluate_guess(combination, guess):
    length = len(combination)
    num_white = 0
    num_black = 0
    tracked_combination = [0] * length
    tracked_guess = [0] * length
    # first pass: check for matches at same position
    for i in range(0, length):
        if combination[i] == guess[i]:
            num_white += 1
            tracked_combination[i] = 1
            tracked_guess[i] = 1
    # second pass: check for matches at other position
    for i in range(0, length):
        if tracked_guess[i] == 0:
            for j in range(0, length):
                if (combination[j] == guess[i]) & (tracked_combination[j] == 0):
                    tracked_guess[i] = 1
                    tracked_combination[j] = 1
                    num_black += 1
    print(f"The guess resulted in {num_white} white and {num_black} black pegs")
    return num_white, num_black


def input_combination(possible_colors):
    print(f"Please input a combination. The colors are: {possible_colors}")
    combination = []
    txt = "Color of peg {} "
    for i in range(1,6):
        color_new = input(txt.format(i))
        while color_new not in possible_colors:
            message = "{} is not a possible color. Please choose again: "
            color_new = input(message.format(color_new))
        combination.append(color_new)
    return combination


def computer_guesses(possible_colors):
    print("I will try to guess your combination.")
    combination = input_combination(possible_colors)
    print("Guessing combination...")
    guess = create_random_combination(possible_colors, len(combination))
    print(f'Guessing... {guess}')
    num_white, num_black = evaluate_guess(combination, guess)
    if num_white == 5:
        print("I have guessed the combination!")


def user_guesses(possible_colors):
    combination = create_random_combination(possible_colors, 5)
    print("Try to guess my combination!")
    guess = input_combination(possible_colors)
    num_white, num_black = evaluate_guess(combination, guess)
    while num_white != 5:
        print("Try again!")
        guess = input_combination(possible_colors)
        num_white, num_black = evaluate_guess(combination, guess)
    print("You've guessed it!!")

def main():
    possible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'brown', 'black']

    user_guesses(possible_colors)


main()
