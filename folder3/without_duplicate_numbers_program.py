#Batch 3 - Program 1

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

print("Out of the ten numbers entered, the number/s that doesn't/don't have a duplicate is/are:")

for num in num_list:
    if num_list.count(num) == 1:
        print(num)