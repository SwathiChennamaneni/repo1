#40. WAP to find union and intersection of lists.

list1 = [1,2,3]
list2 = [3,4,5]
Intersection_List = []
Union_List = []
for i in list1:
	if i in list2:
		Intersection_List.append(i)
print "Intersection List:",Intersection_List
for j in list2:
    if j not in list1:
        list1.append(j)
print "Union List:",list1
