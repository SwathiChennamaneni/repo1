#83. find out intersection, union, difference of two list without/with using set

list1 = [1,2,3]
list2 = [3,4,5]
Intersection_List = []
Difference_List = []
Difference_List = list1
'''Intersection of List1 and List2'''
for i in list1:
	if i in list2:
		Intersection_List.append(i)
print "Intersection of Lists:",Intersection_List
'''Union of List1 and List2'''
for j in list2:
    if j not in list1:
        list1.append(j)
print "Union of List:",list1
'''Difference of List1 and List2'''
for i in Difference_List:
    if i in list2:
        Difference_List.remove(i)
print "difference of two List1 and List2:",Difference_List
