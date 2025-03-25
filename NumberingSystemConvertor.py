#20230170 ساندي عماد وليم
#20230134 ديمه خالد علام
#20230140روان رشدي فتحي
def decimal_to_binary():
    num = int(input("Enter a decimal number:"))
    result = ""
    while (num) > 0:
        reminder = (num) % 2
        result = str(reminder) + result
        num = (num) // 2
    print("the binary number is: ",result)
    return result

def decimal_to_octal():
    num = int(input("Enter a decimal number:"))
    result = ""
    while (num) > 0:
        reminder = (num) % 8
        result = str(reminder) + result
        num = (num) // 8
    print("The octal number is: ",result)

def binary_to_decimal():
    num = int(input("Enter a binary number:"))
    decimal = 0
    i = 0
    while (num) > 0:
        digit = (num) % 10
        decimal = decimal + digit * (2 ** i)
        num = (num) // 10
        i = i + 1
    print("The decimal number is: ",decimal)

def octal_to_decimal():
    num = int(input("Enter a octal number:"))
    decimal = 0
    i = 0
    while (num) > 0:
        digit = (num) % 10
        decimal = decimal + digit * (8 ** i)
        num = (num) // 10
        i = i + 1
    print("The decimal number is: ",decimal)

def binary_to_octal():
    # From binary to octal
    # 1st step convert from binary to decimal
    num = input("enter a binary number:")
    decimal = 0
    i = 0
    while int(num) > 0:
        digit = int(num) % 10
        decimal = decimal + digit * (2 ** i)
        num = int(num) // 10
        i = i + 1
    # print(decimal)
    # 2nd step convert from decimal to octal
    result = ""
    while decimal > 0:
        reminder = decimal % 8
        result = str(reminder) + result
        decimal = decimal // 8
    print("The octal number is: ",result)

def octal_to_binary():
    # From octal to binary
    # 1st step convert from octal to decimal
    num = input("Enter a octal number:")
    decimal = 0
    i = 0
    while int(num) > 0:
        digit = int(num) % 10
        decimal = decimal + digit * (8 ** i)
        num = int(num) // 10
        i = i + 1
    # print(decimal)
    # 2nd step convert from decimal to binary
    result = ""
    while decimal > 0:
        reminder = decimal % 2
        result = str(reminder) + result
        decimal = decimal // 2
    print("The binary number is: ",result)

def decimal_to_hexadecimal():
    num = input("Enter a decimal number:")
    result = ""
    while int(num) > 0:
        reminder = int(num) % 16
        if reminder > 9:
            if reminder == 10:
                reminder = "A"
            if reminder == 11:
                reminder = "B"
            if reminder == 12:
                reminder = "C"
            if reminder == 13:
                reminder = "D"
            if reminder == 14:
                reminder = "E"
            if reminder == 15:
                reminder = "F"
        result = str(reminder) + result
        num = int(num) // 16
    print("The hexadecimal number is:",result)

def binary_to_hexadecimal():
    # From binary to hexadecimal
    # 1st step convert from binary to decimal
    num = input("Enter a binary number:")
    decimal = 0
    i = 0
    while int(num) > 0:
        digit = int(num) % 10
        decimal = decimal + digit * (2 ** i)
        num = int(num) // 10
        i = i + 1
    # print(decimal)
    # 2nd step convert from decimal to hexadecimal
    result = ""
    while decimal > 0:
        reminder = decimal % 16
        if reminder > 9:
            if reminder == 10:
                reminder = "A"
            if reminder == 11:
                reminder = "B"
            if reminder == 12:
                reminder = "C"
            if reminder == 13:
                reminder = "D"
            if reminder == 14:
                reminder = "E"
            if reminder == 15:
                reminder = "F"
        result = str(reminder) + result
        decimal = decimal // 16
    print("The hexadecimal number is: ",result)

def octal_to_hexadecimal():
    # From octal to hexadecimal
    # 1st from octal to decimal
    num = input("Enter a octal number:")
    decimal = 0
    i = 0
    while int(num) > 0:
        digit = int(num) % 10
        decimal = decimal + digit * (8 ** i)
        num = int(num) // 10
        i = i + 1
    # print(decimal)
    # 2nd from decimal to hexadecimal
    result = ""
    while decimal > 0:
        reminder = decimal % 16
        if reminder > 9:
            if reminder == 10:
                reminder = "A"
            if reminder == 11:
                reminder = "B"
            if reminder == 12:
                reminder = "C"
            if reminder == 13:
                reminder = "D"
            if reminder == 14:
                reminder = "E"
            if reminder == 15:
                reminder = "F"
        result = str(reminder) + result
        decimal = decimal // 16
    print("The hexadecimal number is:",result)

def hexadecimal_to_decimal():
    num = input("Enter the hexadecimal number:")
    i = len(num) - 1
    decimal = 0
    for x in num:
        if x == "A":
            x = 10
        elif x == "B":
            x = 11
        elif x == "C":
            x = 12
        elif x == "D":
            x = 13
        elif x == "E":
            x = 14
        elif x == "F":
            x = 15
        else:
            x = int(x)
        decimal = decimal + x * (16 ** i)
        i = i - 1
    print("The decimal number is:",decimal)

def hexadecimal_to_binary():
    # From hexadecimal to binary
    # 1st from hexadecimal to decimal
    num = input("Enter a hexadecimal number:")
    i = len(num) - 1
    decimal = 0
    for x in num:
        if x == "A":
            x = 10
        elif x == "B":
            x = 11
        elif x == "C":
            x = 12
        elif x == "D":
            x = 13
        elif x == "E":
            x = 14
        elif x == "F":
            x = 15
        else:
            x = int(x)
        decimal = decimal + x * (16 ** i)
        i = i - 1
    # print(decimal)
    # 2nd from decimal to binary
    result = ""
    while decimal > 0:
        reminder = decimal % 2
        result = str(reminder) + result
        decimal = decimal // 2
    print("The binary number is:",result)

def hexadecimal_to_octal():
    # From hexadecimal to octal
    # 1st from hexadecimal to decimal
    num = input("Enter a hexadecimal number")
    i = len(num) - 1
    decimal = 0
    for x in num:
        if x == "A":
            x = 10
        elif x == "B":
            x = 11
        elif x == "C":
            x = 12
        elif x == "D":
            x = 13
        elif x == "E":
            x = 14
        elif x == "F":
            x = 15
        else:
            x = int(x)
        decimal = decimal + x * (16 ** i)
        i = i - 1
    # print(decimal)
    # 2nd from decimal to octal
    result = ""
    while decimal > 0:
        reminder = decimal % 8
        result = str(reminder) + result
        decimal = decimal // 8
    print("The octal number is:",result)

print("** Numbering system converter **")
def menu1():
    print("[A] Insert a new number\n[B] Exit the program ")
menu1()
choice = input("Please enter your choice(A/B)")
while choice != "B":
     if choice == "A":
        print("** Please select the base you want to convert a number from **")
        def menu2():
            print("[A] Decimal\n[B] Binary\n[c] octal\n[D] Hexadecimal")
        menu2()
        choice2 = input("Please enter your choice (A/B/C/D)")
        if choice2 == "A" or choice2 == "B" or choice2 == "C" or choice2 == "D":
            print("** Please select the base you want to convert a number to **")
            def menu3():
                print("[A] Decimal\n[B] Binary\n[C] Octal\n[D] Hexadecimal")
            menu3()
            choice3 = input("Please enter your choice (A/B/C/D)")
            if choice3 == "A" or choice3 == "B" or choice3 == "C" or choice3 == "D":
                if choice2 == "A" and choice3 == "B":
                    # From decimal to binary
                    decimal_to_binary()
                if choice2 == "A" and choice3 == "C":
                    # From decimal to octal
                    decimal_to_octal()
                if choice2 == "B" and choice3 == "A":
                   # From binary to decimal
                   binary_to_decimal()
                if choice2 == "C" and choice3 == "A":
                   # From octal to decimal
                   octal_to_decimal()
                if choice2 == "B" and choice3 == "C":
                   # From binary to octal
                   binary_to_octal()
                if choice2 == "C" and choice3 == "B":
                    # From octal to binary
                    octal_to_binary()
                if choice2 == "A" and choice3 == "D":
                    # From decimal to hexadecimal
                    decimal_to_hexadecimal()
                if choice2 == "B" and choice3 == "D":
                   # From binary to hexadecimal
                   binary_to_hexadecimal()
                if choice2 == "C" and choice3 == "D":
                    # From octal to hexadecimal
                    octal_to_hexadecimal()
                if choice2 == "D" and choice3 == "A":
                    # From hexadecimal to decimal
                    hexadecimal_to_decimal()
                if choice2 == "D" and choice3 == "B":
                    # From hexadecimal to binary
                    hexadecimal_to_binary()
                if choice2 == "D" and choice3 == "C":
                   # From hexadecimal to octal
                   hexadecimal_to_octal()
            else:
                print("Please select a valid choice")
        else:
            print("Please select a valid choice")
     else:
         print("Please select a valid choice.")
     choice = input("Enter your choice(A/B)")
print("End of program.")
