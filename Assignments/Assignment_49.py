#49. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even

input1 = [1,2,3,4,5,6,8,10]
new_list = []
for i in input1:
    if i % 2 == 0:
        new_list.append("Even")
    else:
        new_list.append("Odd")            
print new_list
