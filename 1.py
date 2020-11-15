def number_guessing():
    '''
    Number guessing game.
    :return: "You win!"
    '''
    import random
    random_number = random.randint(1, 101)

    while True:

        entered_number = input("Guess the number:")

        try:
            entered_number = float(entered_number)
        except ValueError:
            print("It's not a number!")

        try:
            if entered_number < random_number:
                print("Too small!")


            elif entered_number > random_number:
                print("Too big!")

            elif entered_number == random_number:
                return "You win!"
        except TypeError:
            print("You cannot compare it with a number!")

print(number_guessing())

    



























