'''
This program collects three out of the four unknown variables of simple interest and calculates the last one.
E.g. It'll receive inputs for the simple interest, principal and rate then calculate the time.
'''

print ('''Which variable do you wish to calculate:
1. Simple Interest
2. Principal
3. Rate (Percentage)
4. Time (in years)
- You can't find a variable without knowing three other variables.
''')

choice = input("Ener a choice:  ")
if choice.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()
choice = int(choice)

if choice == 1:
    principal = input("Enter the principal (digits only): ")
    rate = input("Enter the rate (digits only): ")
    time = input("Enter the time (digits only): ")
    if principal.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if rate.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if time.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    principal = int(principal)
    rate = int(rate)
    time = int(time)
    
    numerator = principal*rate*time
    SimpleInterest = numerator/100
    print ("The simple interst is",SimpleInterest)
elif choice == 2:
    SimpleInterest = input("Enter the simple interest (digits only): ")
    rate = input("Enter the rate (digits only): ")
    time = input("Enter the time (digits only): ")
    if SimpleInterest.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if rate.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if time.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    SimpleInterest = int(SimpleInterest)
    rate = int(rate)
    time = int(time)

    numerator = SimpleInterest*100
    denominator = rate*time
    principal = numerator/denominator
    print ("The principal is",principal)
elif choice == 3:
    SimpleInterest = input("Enter the simple interest (digits only): ")
    principal = input("Enter the principal (digits only): ")
    time = input("Enter the time (digits only): ")
    if SimpleInterest.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if principal.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if time.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    SimpleInterest = int(SimpleInterest)
    principal = int(principal)
    time = int(time)

    numerator = SimpleInterest*100
    denominator = principal*time
    rate = numerator/denominator
    print ("The rate is",rate)
elif choice == 4:
    SimpleInterest = input("Enter the simple interest (digits only): ")
    principal = input("Enter the principal (digits only): ")
    rate = input("Enter the rate (digits only): ")
    if SimpleInterest.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if principal.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    if rate.isdigit():
        print()
    else:
        print("You didn't enter a valid number.")
        exit()
    SimpleInterest = int(SimpleInterest)
    principal = int(principal)
    rate = int(rate)

    numerator = SimpleInterest*100
    denominator = principal*rate
    time = numerator/denominator
    print ("The rate is",time)
else:
    print("You did not enter a valid number.")

#If you loved this or you're looking for more of this, check https://github.com/De-ORaCle
#Don't forget to follow me.
