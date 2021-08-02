print('''This program solves quadratic quations.

Quadratic equations naturally are in a format:
    ax^2 + bx + c = 0
All you have to do is input the values for a, b and c, then you get your answer.''')

a = input("Enter the value for 'a': ")
a = int(a)
b = input ("Enter the value for 'b': ")
b = int(b)
c = input("Enter the value for 'c':  ")
c = int(c)

z = -1 * b
y = b ** 2
u = 4 * a * c
v = 2 * a
w = y - u
s = w ** 0.5
t = z + s
m = z - s
#constructed the quadratic formula

x = t/v
d = m/v

print ("The values of your quadratic equation are", x ,"and", d)

#If you loved this or you're looking for more of this, check https://github.com/De-ORaCle
#Don't forget to follow me.
