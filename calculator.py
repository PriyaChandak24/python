class calculator:
    def addition(self):
        print(x + y)
    def subtraction(self):
        print(x - y)
    def multiplication(self):
        print(x * y)
    def division(self):
        print(x / y)
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
obj1 = calculator()
choice = 1
while choice !=0:
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj1.addition())
    elif choice == 2:
        print(obj1.subtraction())
    elif choice == 3:
        print(obj1.multiplication())
    elif choice == 4:
        print(obj1.division())
    else:
        print("Invalid choice")
