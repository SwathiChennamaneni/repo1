#43. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]

#With Imbuilt Function
a=[1,2,3,2,3,4,1,3,4]
b=set(a)
print "Removed Duplicates(Method1):",b
#Without using Imbuilt Function
a=[1,2,3,2,3,4,1,3,4]
list2 = []
for i in a:
    if i not in list2:
        list2.append(i)
    else:
        continue
print "Removed Duplicates(Method2):",list2
