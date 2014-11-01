message=input("PLease enter a message to repeat:")
numberRepeat=int(input("Please enter the amount of times for the message to repeat:"))
repeat=numberRepeat+1
for count in range(1,repeat):
    print(message)
