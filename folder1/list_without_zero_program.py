#Batch 1 - Program 10

num_list = []

for i in range(101):
    if i % 10 != 0:
        num_list.append(i)

print(f"The list of numbers from 0 to 100, except those ending in 0, is: {num_list}")