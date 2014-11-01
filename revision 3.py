total=0
amount2average=int(input("Please enter amount of numbers you would like to average:"))
amountaverage=amount2average+1
for count in range(1,amountaverage):
    number=int(input("Please enter a number:"))
    total=total+number
average=total/amount2average
print("The average of is {0}.".format(average))
