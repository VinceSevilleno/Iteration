answer = False
while not answer:
    number = int(input("Please enter a number between the range of 10 to 20:"))
    
    if 10 <= number <= 20:
        answer = True
        print("You have entered a number within the range of 10 and 20.")
