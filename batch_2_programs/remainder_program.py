#Batch 2 - Program 5

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if num_2 == 0:
    print("Undefined; cannot divide by zero.")
else:
    remainder = num_1 % num_2
    print(f"The remainder of {num_1} divided by {num_2} is: {remainder}")