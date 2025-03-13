#Batch 2 - Program 10

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

begin = min(num_1, num_2) + 1
end = max(num_1, num_2)

print(f"The number/s between {num_1} and {num_2} is/are:")

for i in range(begin, end):
    print(i)