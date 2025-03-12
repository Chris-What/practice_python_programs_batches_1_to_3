#Batch 2 - Program 7

even_count = 0

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_count += 1

print(f"Out of the ten numbers entered, {even_count} of them is/them are even.")