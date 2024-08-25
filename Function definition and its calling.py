
#function defining
def add(num1,num2):
    return  num1 + num2
def sub(num1,num2):
    return  num1 - num2
def multiply(num1,num2):
    return  num1 * num2
def divide(num1,num2):
    return  num1 / num2
#list
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")
#input from user
choice= int(input("Enter a number (1/2/3/4) : "))


#collection values for calculation

num1=float(input("Enter the first value : "))
num2=float(input("Enter the first value : ")) 

if choice == 1 :
    print(f"Result is {add(num1,num2)}")
elif choice == 2 :
    print(f"Result is {sub(num1,num2)}")
elif choice == 3:
    print(f"Result is {multiply(num1,num2)}")
elif choice == 4:
    print(f"Result is {divide(num1,num2)}")
else:
    print("Invalid input")