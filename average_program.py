#Batch 4 - Program 5

sum = 0
num_count = 0

while True:
    try:
        num = float(input("Enter a number: "))
        sum += num
        num_count += 1
    
    except ValueError:
        average = sum / num_count
        print(f"The average of all numbers entered is: {average}.")
        break