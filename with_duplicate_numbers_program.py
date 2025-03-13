#Batch 4 - Program 1

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

print("Out of the ten numbers entered, the number/s that has/have a duplicate is/are:")

alr_printed = set()
for num in num_list:
    if num_list.count(num) > 1 and num not in alr_printed:
        print(num)
        alr_printed.add(num)