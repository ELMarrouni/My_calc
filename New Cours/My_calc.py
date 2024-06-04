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
            print("Please enter a valid number")  # Prompt the user again


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
            print("Please enter just a number")  # Prompt the user again


def Arithmetic():
    while True:
        a = input("Enter the Arithmetic symbol: ")
        try:
            if a == "+" or a == "-" or a == "*" or a == "/":
                return a
            else:
                print("Please enter an arithmetic symbol \n'* or + or / or -'")
        except ValueError:
            print("Please enter an arithmetic symbol \n'* or + or / or -'")


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
# Arithmetic()
