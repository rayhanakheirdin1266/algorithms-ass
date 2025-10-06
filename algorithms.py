
def factorial(n):
    """
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
    Time Complexity: O(n)
    """
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def linear_search(numbers, target):
    """
    Time Complexity: O(n)
    """
    for num in numbers:
        if num == target:
            return True
    return False


def fibonacci_iterative(n):
    """
    Returns the nth Fibonacci number using iteration.
    Time Complexity: O(n)
    """
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a=0
    b=1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def fibonacci_recursive(n):
    """
    Returns the nth Fibonacci number using recursion.
    Time Complexity: O(2^n)
    """
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


USERNAME = "Rayhana"
PASSWORD = "@@1234@@"

is_logged_in = False


def login():
    """
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
                print("Factorial of", n, "is:", factorial(n), "\n")

    elif choice == "2":
        if not is_logged_in:
            print("Please log in first.\n")
        else:
            nums = input("Enter numbers separated by spaces: ").strip()
            parts = nums.split()
            valid = True
            for p in parts:
                if not p.lstrip('-').isdigit():
                    valid = False
                    break

            if not valid:
                print("Please enter valid integers only.\n")
            elif len(parts) == 0:
                print("The list is empty.\n")
            else:
                num_list = list(map(int, parts))
                print("The maximum number is:", find_max(num_list), "\n")

    elif choice == "3":
        if not is_logged_in:
            print("Please log in first.\n")
        else:
            nums = input("Enter numbers separated by spaces: ").strip()
            parts = nums.split()
            valid = True
            for p in parts:
                if not p.lstrip('-').isdigit():
                    valid = False
                    break

            if not valid:
                print("Please enter valid integers only.\n")
            elif len(parts) == 0:
                print("The list is empty.\n")
            else:
                num_list = list(map(int, parts))
                target_input = input("Enter the number to search for: ").strip()
                if target_input.lstrip('-').isdigit():
                    target = int(target_input)
                    found = linear_search(num_list, target)
                    if found:
                        print(f"{target} is found in the list.\n")
                    else:
                        print(f"{target} is NOT found in the list.\n")
                else:
                    print("Please enter a valid integer to search.\n")

    elif choice == "4":
        if not is_logged_in:
            print("Please log in first.\n")
        else:
            n = input("Enter a non-negative integer: ").strip()
            if not n.isdigit():
                print("Please enter a valid non-negative integer.\n")
            else:
                n = int(n)
                if n > 30:
                    print("Warning: Recursive Fibonacci is slow for large n. Please enter n ≤ 30.\n")
                print(f"Fibonacci of {n} (iterative): {fibonacci_iterative(n)}")
                print(f"Fibonacci of {n} (recursive): {fibonacci_recursive(n)}\n")

    elif choice == "5":
        login()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 6.\n")

    show_menu()
