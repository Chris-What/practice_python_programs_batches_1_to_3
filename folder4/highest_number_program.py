#Batch 4 - Program 3

highest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if highest is None or num > highest:
            highest = num

    except ValueError:
        print(f"Out of all the numbers entered, the highest number entered is: {highest}")
        break