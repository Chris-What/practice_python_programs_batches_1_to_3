#Batch 3 - Program 3

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        if num_list.count(num) == 0:
            print("Unique")
        else:
            print("Duplicate")
        num_list.append(num)

    except ValueError:
        print("Invalid input.")
        break