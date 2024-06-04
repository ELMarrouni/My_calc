text = "The Result is : "


def firte():
    """
    This function prompts the user to enter a first number and
    returns the number as an integer. If the user enters an invalid
    input, it raises a ValueError and prompts the user again.

    Returns:
        int: The first number entered by the user.
    """
    while True:
        n1 = input("Enter the first number : ")  # Prompt the user to enter a number
        try:
            result_1 = int(n1)  # Convert the input to an integer
            return result_1  # Return the number
        except ValueError:  # If the input is not a valid number
            print("Please enter a just numbers")  # Prompt the user again


def seconde():
    """
    This function prompts the user to enter a second number and
    returns the number as an integer. If the user enters an invalid
    input, it raises a ValueError and prompts the user again.

    Returns:
        int: The second number entered by the user.
    """
    while True:
        n2 = input("Enter the second number : ")  # Prompt the user to enter a number
        try:
            result_2 = int(n2)  # Convert the input to an integer
            return result_2
        except ValueError:  # If the input is not a valid number
            print("Please enter just numbers")  # Prompt the user again


def Arithmetic():
    """
    This function prompts the user to enter an arithmetic symbol
    and returns the symbol as a string. If the user enters an invalid
    input, it raises a ValueError and prompts the user again.

    Returns:
        str: The arithmetic symbol entered by the user.
    """
    while True:
        # Prompt the user to enter an arithmetic symbol
        a = input("Enter the Arithmetic symbol: ")
        try:
            # Check if the symbol is one of the valid arithmetic symbols
            if a in ["+", "-", "*", "/"]:
                return a
            else:
                # Prompt the user to enter a valid arithmetic symbol
                print("Please enter an arithmetic symbol \n'+ or - or * or /'")
        except ValueError:
            # Prompt the user to enter a valid arithmetic symbol
            print("Please enter an arithmetic symbol \n'+ or - or * or /'")


def calculetare():
    result_1 = firte()
    Arit = Arithmetic()
    result_2 = seconde()
    while True:
        if Arit == "+":
            print(text)
            add_results = result_1 + result_2
            print(add_results)
            return calculetare()
        elif Arit == "-":
            print(text)
            sub_results = result_1 - result_2
            print(sub_results)
            return calculetare()
        elif Arit == "/":
            print(text)
            Div_results = result_1 % result_2
            print(Div_results)
            return calculetare()
        elif Arit == "*":
            Mul_results = result_1 * result_2
            print(f"{text} {Mul_results}")
            return calculetare()


calculetare()
