number2average=int(input("Please enter the amount of series of numbers you would like to average:"))
total=0
number=0
print("Once you have enter the amount of numbers you want to average, to get the average TYPE -1")
while number!=-1:
    number=int(input("Please enter a number to average:"))
    if number>0:
        total=total+number
average=total/number2average
print(average)
