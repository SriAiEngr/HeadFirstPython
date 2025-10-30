while True:
    user_input = input("Enter a number: ")
    if user_input == "q":
        break
    try:
        number = float(user_input)
        print("The number is:", number)
    except ValueError:
        print("Invalid input. Please enter a number.")