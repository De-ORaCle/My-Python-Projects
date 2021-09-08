while True:
    print("solving area of plain shapes\n") 
    choice = input("In small letter, input the plain shape you want to calculate: \n")
    if choice == "triangle":
        a = 0.5
        b = float(input("Input the breath digit: "))
        h = float(input("Input the hieght digit: "))
        result = a*b*h
        print("AREA = \n",result)
        
    elif choice == "rectangle" or choice == "square" or choice == "rhombus" or choice == "kite":
        l1 = float(input("Input the first lenght: "))
        l2 = float(input("Input the second lenght: ")) 
        result = l1*l2
        print("AREA = \n",result)

    elif choice == "circle":
        pie = 22/7
        r = float(input("Input your radius: "))
        result = pie*r*r
        print("AREA = \n",result)        
        
    elif choice == "trapezium":
        c = 0.5
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        h = float(input("input height: "))
        result = c*(a+b)*h
        print("AREA = \n",result)

    else:
        print("invalid input")
