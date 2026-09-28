tasks = []

print("Welcome to My Personal Mini-Toolkit!")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Simple Calculator: performs basic math with two numbers.
        print("\n--- Simple Calculator ---")

        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Sorry, you cannot divide by zero.")
                continue
        else:
            print(f"Sorry, {operator} is not a valid operation.")
            continue

        print(f"The answer is {result}.")

    elif choice == "2":
        # To-Do List: lets the user add, view, and remove tasks.
        while True:
            print("\n--- To-Do List ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":
                task = input("Enter a task: ")
                tasks.append(task)
                print(f"Task '{task}' was added.")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif task_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' was removed.")
                    else:
                        print("That task number does not exist.")

            elif task_choice == "4":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, {task_choice} is not a valid choice.")

    elif choice == "3":
        # Number Guessing Game: asks the user to guess a secret number.
        secret_number = 7
        attempts = 0

        print("\n--- Number Guessing Game ---")
        print("Guess the secret number between 1 and 10.")

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

    elif choice == "4":
        print("Thanks for using My Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, {choice} is not a valid choice. Please try again.")