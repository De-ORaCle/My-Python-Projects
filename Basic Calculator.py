def add(x, y):
      return x + y

def subtract(x, y):
      return x - y

def mulltiply(x, y):
      return x * y

def divide(x, y):
      return x / y

def exponential(x, y):
      return x ** y

def cube(x):
      return x * x * x

print ("Select operation.")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
print ("5. Exponential")
print ("6. Cube")

while True:
      choice = input ("Enter choice(1/2/3/4/5/6): ")

      if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                  print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                  print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                  print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                  print(num1, "/", num2, "=", divide(num1, num2))

            elif  choice == '5':
                  print(num1, "^", num2, "=", exponential(num1, num2))
            break
      
      elif choice in ('6'):
            num1 = float(input("Enter a number: "))

            if choice == '6':
                  print(num1, "*", num1, "*", num1, "=", cube(num1))
      else:
            print("Invalid Input")

#If you loved this or you're looking for more of this, check https://github.com/De-ORaCle
#Don't forget to follow me.


