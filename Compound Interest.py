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

n = input('''Enter the compound (n), that is, how many times a year: ''')
if n.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()

t = input("Enter the time (t in years): ")
if t.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()

P = int(P)
r = int(r)
n = int(n)
t = int(t)

br = r/n
brr = 1 + br
brrr = brr**(n*t)
A = P*brrr

print ("\n\nThe compound interest is",A)

#If you loved this or you're looking for more of this, check https://github.com/De-ORaCle
#Don't forget to follow me.
