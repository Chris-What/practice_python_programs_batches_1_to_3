#Batch 3 - Program 4

lowest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num
    
    except ValueError:
        print(f"The lowest number entered is: {lowest}.")
        break