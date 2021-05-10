import random


def guess_combination(possible_colors, colors):
    guess = []
    for i in range(0, len(colors)):
        guess.append(random.choice(possible_colors))
    print(f'Guessing... {guess}')
    if guess==colors:
        print('Guessed correct combination!')
    else:
        print('Wrong combination.')
    return


def main():
    print("Welcome to Mastermind, please choose the colors of your pegs. The colors are: red, orange, yellow, green, blue, white, brown, black")
    possible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'brown', 'black']
    colors = []
    txt = "Color of peg {} "
    for i in range(1,6):
        color_new = input(txt.format(i))
        while color_new not in possible_colors:
            message = "{} is not a possible color. Please choose again: "
            color_new = input(message.format(color_new))
        colors.append(color_new)
    print("Guessing combination...")
    guess_combination(possible_colors, colors)


main()
