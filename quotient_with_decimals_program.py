#Batch 1 - Program 5

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if num_2 == 0:
    print("Undefined; cannot divide by zero.")
else:
    quotient = num_1 / num_2
    print(f"The quotient of the two numbers is: {quotient}.")