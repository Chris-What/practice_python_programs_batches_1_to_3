#Batch 4 - Program 2

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        break

most_duplicates = max(set(num_list), key=num_list.count)

print(f"Out of all the numbers entered, the number with the most duplicates is: {most_duplicates}.")