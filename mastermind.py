


def main():
    print("Welcome to Mastermind, please choose the colors of your pegs. Valid colors are: red, orange, yellow, green, blue, white, brown, black")
    colors = []
    txt = "Color of peg {} "
    for i in range(1,6):
        colors.append(input(txt.format(i)))
    print(colors)

main()