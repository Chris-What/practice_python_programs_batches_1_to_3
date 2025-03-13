#Batch 3 - Program 2

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num not in num_list:
        num_list.append(num)

print("The list of numbers entered, except duplicates, is:")

for num in num_list:
    print(num)