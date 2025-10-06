
def factorial(n):
    """
    Returns the factorial of n (n!) using a loop.
    Time Complexity: O(n)
    """
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def find_max(numbers):
    """
    Returns the largest number in the list using a loop.
    Time Complexity: O(n)
    """
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


USERNAME = "Rayhana"
PASSWORD = "1234"

is_logged_in = False


def login():
    """
    Prompts the user for login credentials.
    Time Complexity: O(1)
    """
    global is_logged_in
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == USERNAME and password == PASSWORD:
        print("Login successful.\n")
        is_logged_in = True
    else:
        print("Invalid credentials.\n")

def show_menu():
    print("Choose an option:")
    print("1. Factorial")
    print("2. Find Max")
    print("3. Linear Search")
    print("4. Fibonacci")
    print("5. Login")
    print("6. Exit")



show_menu()

while True:
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        if not is_logged_in:
            print("Please log in first.\n")
        else:
            n = input("Enter a non-negative integer: ")
            if not n.isdigit():
                print("Please enter a valid non-negative integer.\n")
            else:
                n = int(n)
                if n < 0:
                    print("Factorial is not defined for negative numbers.\n")
                else:
                    print("Factorial of", n, "is:", factorial(n), "\n")

    elif choice == "2":
        if not is_logged_in:
            print("Please log in first.\n")
        else:
            nums = input("Enter numbers separated by spaces: ").strip()
            parts = nums.split()
            if len(parts) == 0:
                print("The list is empty.\n")
            else:
                try:
                    num_list = list(map(int, parts))
                    print("The maximum number is:", find_max(num_list), "\n")
                except ValueError:
                    print("Please enter valid integers only.\n")

    elif choice == "3":
        print("Linear Search: Coming soon...\n")

    elif choice == "4":
        print("Fibonacci: Coming soon...\n")

    elif choice == "5":
        login()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 6.\n")

    # Show the menu again after each loop iteration
    show_menu()
