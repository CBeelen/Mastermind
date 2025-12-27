import numpy as np
from itertools import product
import random

from mastermind import GameHistory, evaluate_guess, guess_random_remaining, weed_out_combs

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



