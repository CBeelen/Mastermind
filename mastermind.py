import random
from argparse import ArgumentParser
from itertools import product

POSSIBLE_COLOURS = ['red', 'green', 'blue', 'white', 'black', 'yellow', 'orange', 'brown', 'pink']

class GameHistory:
    def __init__(self):
        self.history = dict()
        self.num_guesses = 0

    def add_guess(self, num_black, num_white, guess):
        self.history[guess] = (num_black, num_white)
        self.num_guesses += 1


def evaluate_guess(combination, guess):
    # first pass: check for matches at same position
    num_pos = 0  # correct guess
    for i in range(len(guess)):
        if combination[i] == guess[i]:
            num_pos += 1
    # second pass: check for matches at any position
    num_cols = 0
    combination_mod = list(combination)
    for peg in guess:
        if peg in combination_mod:
            num_cols += 1
            combination_mod.remove(peg)
    return num_pos, num_cols-num_pos


def guess_random_remaining(combinations_left):
    idx = random.randint(0, len(combinations_left)-1)
    return combinations_left[idx]


def weed_out_combs(combinations_left_in, guess, num_black_guess, num_white_guess):
    combinations_left_out = combinations_left_in.copy()
    for combination in combinations_left_in:
        num_black, num_white = evaluate_guess(combination, guess)
        if num_black == num_black_guess and num_white == num_white_guess:
            continue
        else:
            combinations_left_out.remove(combination)
    return combinations_left_out


def input_combination(num_colors, combination_length):
    print(f"Please input a combination of length {combination_length}.\n"
          f"The colours are: {POSSIBLE_COLOURS[:num_colors]}")
    combination = []
    txt = "Colour of peg {} "
    for i in range(1,combination_length+1):
        color_new = input(txt.format(i))
        while color_new not in POSSIBLE_COLOURS[:num_colors]:
            message = "{} is not a possible colour. Please choose again: "
            color_new = input(message.format(color_new))
        combination.append(color_new)
    combination_final = tuple(combination)
    return combination_final


def computer_guesses(num_colors, combination_length):
    print("I will try to guess your combination.")
    combination = input_combination(num_colors, combination_length)

    combinations_left = list(product(POSSIBLE_COLOURS[:num_colors], repeat=combination_length))
    game_history = GameHistory()
    while len(combinations_left) > 0:
        print(f'number of combinations left: {len(combinations_left)}')
        guess = guess_random_remaining(combinations_left)
        num_black, num_white = evaluate_guess(combination, guess)
        game_history.add_guess(num_white, num_black, guess)
        print(f'guess {game_history.num_guesses}: {guess}, {num_black} black, {num_white} white')
        if num_black == len(guess):
            print(f'solved. Combination: {combinations_left[0]}, guesses: {game_history.num_guesses}')
            break
        combinations_left = weed_out_combs(combinations_left, guess, num_black, num_white)


def user_guesses(num_colors, combination_length):
    combination = [POSSIBLE_COLOURS[random.randint(0, num_colors - 1)] for i in range(combination_length)]
    print(combination)
    num_black = -1
    print("Try to guess my combination!")
    while num_black != combination_length:
        if num_black != -1: # all iterations but the first
            print("Try again!")
        guess = input_combination(num_colors, combination_length)
        num_black, num_white = evaluate_guess(combination, guess)
        print(f'You get {num_black} black and {num_white} white pegs')
    print("You've guessed it!!")


def main():
    parser = ArgumentParser()
    parser.add_argument('mode', choices=['user-guesses', 'computer-guesses'], help='Choose mode')
    parser.add_argument('--num_colors', type=int, default=8, help='Choose number of colors')
    parser.add_argument('--combination_length', type=int, default=5,
                        help='Choose length of combination')
    args = parser.parse_args()

    if args.num_colors > 9:
        raise ValueError('num_colors cannot be greater than 9')
    if args.combination_length > 5:
        print('Warning: combination length exceeding 5 can make solver slow')

    if args.mode == 'user-guesses':
        user_guesses(args.num_colors, args.combination_length)
    elif args.mode == 'computer-guesses':
        computer_guesses(args.num_colors, args.combination_length)


if __name__ == "__main__":
    main()
