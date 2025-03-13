#Batch 4 - Program 4

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        print("The list of numbers entered, arranged from highest to lowest, is:")

        num_list.sort(reverse=True)
        for num in num_list:
            print(num)
        break