import random


def guess_combination(possible_colors, length):
    guess = []
    for i in range(0, length):
        guess.append(random.choice(possible_colors))
    print(f'Guessing... {guess}')
    return guess


def evaluate_guess(combination, guess):
    length = len(combination)
    num_white = 0
    num_black = 0
    tracked = [0] * length
    # first pass: check for matches at same position
    for i in range(0, length):
        if combination[i] == guess[i]:
            num_white += 1
            tracked[i] = 1
    # second pass: check for matches at other position
    for i in range(0, length):
        if tracked[i] == 0:
            for j in range(0, length):
                if (combination[j] == guess[i]) & (tracked[j] == 0):
                    tracked[j] = 1
                    num_black += 1
    print(f"The guess resulted in {num_white} white and {num_black} black pegs")
    return num_white, num_black


def main():
    print("Welcome to Mastermind, please choose the colors of your pegs. The colors are: red, orange, yellow, green, blue, white, brown, black")
    possible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'brown', 'black']
    combination = []
    txt = "Color of peg {} "
    for i in range(1,6):
        color_new = input(txt.format(i))
        while color_new not in possible_colors:
            message = "{} is not a possible color. Please choose again: "
            color_new = input(message.format(color_new))
        combination.append(color_new)
    print("Guessing combination...")
    guess = guess_combination(possible_colors, len(combination))
    num_white, num_black = evaluate_guess(combination, guess)


main()
