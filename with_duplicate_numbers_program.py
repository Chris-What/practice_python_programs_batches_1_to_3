#Batch 4 - Program 1

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

print("Out of the ten numbers entered, the number/s that has/have a duplicate is/are:")

printed_num = set()
for num in num_list:
    if num_list.count(num) > 1 and num not in printed_num:
        print(num)
        printed_num.add(num)