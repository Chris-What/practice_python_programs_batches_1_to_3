#Batch 3 - Program 5

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        print("The list of numbers, arranged from lowest to highest, is:")

        num_list.sort()
        for num in num_list:
            print(num)
        break