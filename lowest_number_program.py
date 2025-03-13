#Batch 3 - Program 4

lowest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num
    
    except ValueError:
        print(f"Out of all the numbers entered, the lowest number is: {lowest}.")
        break