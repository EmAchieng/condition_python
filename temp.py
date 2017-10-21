#addition
def addition(a, b):
   return a + b

#subtraction
def subtraction(a, b):
   return a - b

#multiplication
def multiplication(a, b):
   return a * b

#division
def division(a, b):
   return a / b

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")


selection = input("Enter selection(1/2/3/4):")

FirstNumber = int(input("Enter first number: "))
SecondNumber = int(input("Enter second number: "))

if selection == '1':
   print(FirstNumber,"+",SecondNumber,"=", addition(FirstNumber,SecondNumber))

elif selection == '2':
   print(FirstNumber,"-",SecondNumber,"=", subtraction(FirstNumber,SecondNumber))

elif selection == '3':
   print(FirstNumber,"*",SecondNumber,"=", multiplication(FirstNumber,SecondNumber))

elif selection == '4':
   print(FirstNumber,"/",SecondNumber,"=", division(FirstNumber,SecondNumber))
else:
   print("Invalid input")