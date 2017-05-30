#54. write a function to get dynamic list for floating numbers also based on strat and end and step parameters

print "Please Enter None if you dont want to specify Start_Number or Step Value"
Start_Num = input("Enter Start Number:")
End_Num = input("Enter End Number:")
Step = input("Enter Step:")

sum=0
Range_List = []
if str(Start_Num) == "None" and str(Step) == "None":
    print "Default Step is 0.5\n"
    while sum <End_Num:
        Range_List.append(sum)
        sum+=0.5
        if sum == float(End_Num):
            break
elif str(Step) =="None":
    print "Default Step is 0.5\n"
    while Start_Num < End_Num:
        Range_List.append(Start_Num)
        Start_Num+=0.5
        if Start_Num == float(End_Num):
            break
else:
    while Start_Num<=End_Num:
        Range_List.append(Start_Num)
        Start_Num+=Step
        if Start_Num == float(End_Num):
            break
        
print "Dynamic List:", Range_List
