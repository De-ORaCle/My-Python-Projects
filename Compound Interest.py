print("This program help you calculate the final amount of a compound interest when all the necessary parameters are given.\n")

P = input("Enter the initial principal balance: ")
if P.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()

r = input("Enter the annual interest rate: ")
if r.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()
