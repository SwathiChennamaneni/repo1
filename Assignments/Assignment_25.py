#25. findout third occurance of given substring

User_String = raw_input("Enter String:")
Find_Char = raw_input("Enter Char to find:")
list1 = []
for i in range(len(User_String)):
    if Find_Char in User_String[i]:
        list1.append(i)
    else:
        continue
print "Third Occurence of a is at index:",list1[2
