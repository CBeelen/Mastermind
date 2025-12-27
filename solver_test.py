import numpy as np
from itertools import product
import random

class GameHistory:
    def __init__(self):
        self.history = dict()
        self.num_guesses = 0

    def add_guess(self, num_white, num_black, guess):
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

def initial_guess(n_comb_len, n_colors):
    initial_guess = list(range(n_colors))
    random.shuffle(initial_guess)
    return tuple(initial_guess[:n_comb_len])


def weed_out_combs(combinations_left_in, guess, num_black_guess, num_white_guess):
    combinations_left_out = combinations_left_in.copy()
    for combination in combinations_left_in:
        num_black, num_white = evaluate_guess(combination, guess)
        if num_black == num_black_guess and num_white == num_white_guess:
            continue
        else:
            combinations_left_out.remove(combination)
    return combinations_left_out


n_comb_len = 5
n_colors = 8
combination = [random.randint(0, n_colors-1) for i in range(n_comb_len)]
print(f'Combination: {combination}')

combinations_left = list(product(range(n_colors), repeat=n_comb_len))
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



