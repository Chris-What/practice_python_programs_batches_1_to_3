#Batch 4 - Program 5

total = 0
num_count = 0

while True:
    try:
        num = float(input("Enter a number: "))
        total += num
        num_count += 1
    
    except ValueError:
        if num_count == 0:
            print("No number entered.")
            break
        else:
            average = total / num_count
            print(f"The average of all numbers entered is: {average}")
            break