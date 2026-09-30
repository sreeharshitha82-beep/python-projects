def increasing_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def decreasing_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def right_aligned_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


def hollow_square(n):
    for i in range(n):
        for j in range(n):

            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print()


def repeated_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")

        print()


def floyds_triangle(n):
    number = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1

        print()


def alphabet_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")

        print()


def repeated_alphabet_triangle(n):
    for i in range(1, n + 1):
        letter = chr(65 + i - 1)

        for j in range(i):
            print(letter, end=" ")

        print()


def binary_triangle(n):
    for i in range(1, n + 1):

        for j in range(i):

            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")

        print()


def x_pattern(n):
    for i in range(n):

        for j in range(n):

            if j == i or j == n - i - 1:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


def plus_pattern(n):
    middle = n // 2

    for i in range(n):

        for j in range(n):

            if i == middle or j == middle:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


def hollow_triangle(n):
    for i in range(1, n + 1):

        for j in range(1, i + 1):

            if j == 1 or j == i or i == n:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


def pascal_triangle(n):

    for i in range(n):

        print(" " * (n - i), end="")

        number = 1

        for j in range(i + 1):

            print(number, end=" ")

            number = number * (i - j) // (j + 1)

        print()


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n==============================================")
    print("              PATTERN GENERATOR")
    print("==============================================")

    print("1.  Increasing Star Triangle")
    print("2.  Decreasing Star Triangle")
    print("3.  Right-Aligned Triangle")
    print("4.  Pyramid")
    print("5.  Inverted Pyramid")
    print("6.  Diamond")
    print("7.  Hollow Square")
    print("8.  Hollow Triangle")
    print("9.  Number Triangle")
    print("10. Repeated Number Triangle")
    print("11. Floyd's Triangle")
    print("12. Alphabet Triangle")
    print("13. Repeated Alphabet Triangle")
    print("14. Binary Triangle")
    print("15. X Pattern")
    print("16. Plus Pattern")
    print("17. Pascal's Triangle")
    print("18. Exit")

    print("==============================================")


# ============================================================
# MAIN
# ============================================================

def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "18":
            print("\nExiting Pattern Generator. Goodbye!")
            break

        elif choice in {
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15",
            "16", "17"
        }:

            try:
                n = int(input("Enter the size of the pattern: "))

                if n <= 0:
                    print("Size must be greater than 0.")
                    continue

            except ValueError:
                print("Please enter a valid integer.")
                continue


            if choice == "1":
                increasing_triangle(n)

            elif choice == "2":
                decreasing_triangle(n)

            elif choice == "3":
                right_aligned_triangle(n)

            elif choice == "4":
                pyramid(n)

            elif choice == "5":
                inverted_pyramid(n)

            elif choice == "6":
                diamond(n)

            elif choice == "7":
                hollow_square(n)

            elif choice == "8":
                hollow_triangle(n)

            elif choice == "9":
                number_triangle(n)

            elif choice == "10":
                repeated_number_triangle(n)

            elif choice == "11":
                floyds_triangle(n)

            elif choice == "12":
                alphabet_triangle(n)

            elif choice == "13":
                repeated_alphabet_triangle(n)

            elif choice == "14":
                binary_triangle(n)

            elif choice == "15":
                x_pattern(n)

            elif choice == "16":
                plus_pattern(n)

            elif choice == "17":
                pascal_triangle(n)

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()