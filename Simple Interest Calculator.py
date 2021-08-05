'''
This program collects three out of the four unknown variables of simple interest and calculates the last one.
E.g. It'll receive inputs for the simple interest, principal and rate then calculate the time.
'''

print ('''Which variable do you wish to calculate:
1. Simple Interest
2. Principal
3. Rate
4. Time
- You can't find a variable without knowing three other variables.
''')

choice = input("Ener a choice:  ")
if choice.isdigit():
    print()
else:
    print("You didn't enter a valid number.")
    exit()
