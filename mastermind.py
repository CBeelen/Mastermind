import random

POSSIBLE_COLOURS = ('red', 'orange', 'yellow', 'green', 'blue', 'white')
SENARY_DICT = {
        'red': 0,
        'orange': 1,
        'yellow': 2,
        'green': 3,
        'blue': 4,
        'white': 5
    }


class Combination:
    def __int__(self, colors):
        self.senary = translate_to_senary(colors)


def translate_to_senary(colors):
    senary = 0
    for i in range(1,len(colors)+1):
        senary += 6**(i-1) * SENARY_DICT[colors[i-1]]
    return(senary)


def translate_from_senary(senary, combination_length):
    reverse_dict = {number: color for color, number in SENARY_DICT.items()}
    colors = []
    for i in range(1, combination_length+1):
        current = senary % (6**i)
        senary -= current
        colors.append(reverse_dict[current/6**(i-1)])
    return(colors)


def create_random_combination(length):
    random_combination = []
    for i in range(0, length):
        random_combination.append(random.choice(POSSIBLE_COLOURS))
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
                if combination[j] == guess[i] and tracked_combination[j] == 0 and tracked_guess[i] == 0:
                    tracked_guess[i] = 1
                    tracked_combination[j] = 1
                    num_black += 1
    print(f"The guess resulted in {num_white} white and {num_black} black pegs")
    return num_white, num_black


def input_combination():
    print(f"Please input a combination. The colours are: {POSSIBLE_COLOURS}")
    combination = []
    txt = "Colour of peg {} "
    for i in range(1,6):
        color_new = input(txt.format(i))
        while color_new not in POSSIBLE_COLOURS:
            message = "{} is not a possible colour. Please choose again: "
            color_new = input(message.format(color_new))
        combination.append(color_new)
    return combination


def improve_guess(guess, num_white, num_black):
    new_guess = create_random_combination(len(guess))
    for i in range(num_black):
        position = random.randint(0, 4)
        guess_position = random.randint(0, 4)
        new_guess[position] = guess[guess_position]
    for i in range(num_white):
        position = random.randint(0, 4)
        new_guess[position] = guess[position]
    return new_guess


def computer_guesses():
    print("I will try to guess your combination.")
    combination = input_combination()
    num_tries = 0
    num_white = -1
    while num_white != 5 and num_tries < 10:
        if num_white == -1:     # initial guess
            guess = create_random_combination(len(combination))
        else:
            guess = improve_guess(guess, num_white, num_black)
        print(f'Guessing... {guess}')
        num_white, num_black = evaluate_guess(combination, guess)
        num_tries += 1
    if num_white == 5:
        print("I have guessed the combination!")
    else:
        print("I am giving up.")


def user_guesses():
    combination = create_random_combination(5)
    num_white = -1
    print("Try to guess my combination!")
    while num_white != 5:
        if num_white != -1: # all iterations but the first
            print("Try again!")
        guess = input_combination()
        num_white, num_black = evaluate_guess(combination, guess)
    print("You've guessed it!!")


def main():

    colors = input_combination()
    print(colors)
    senary = translate_to_senary(colors)
    print(senary)
    colors_return = translate_from_senary(senary, len(colors))
    print(colors_return)


main()
