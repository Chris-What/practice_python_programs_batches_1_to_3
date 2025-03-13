#Batch 2 - Program 6

num_list = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

difference = num_list[0]
for num in num_list[1:]:
    difference -= num

print(f"The difference of the first number {num_list[0]} minus the rest of the numbers is: {difference}")