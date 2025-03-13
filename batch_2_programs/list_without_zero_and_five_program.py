#Batch 2 - Program 9

num_list = []

for i in range(101):
    if i % 10 != 0 and i % 5 != 0:
        num_list.append(i)

print(f"The list of numbers from 0 to 100, except those ending in 0 or 5, is: {num_list}")