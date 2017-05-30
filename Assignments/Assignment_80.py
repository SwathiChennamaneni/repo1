#80  WAP to remove perticular element from a given list for all occurancers

list1 = [1,2,2,3,3,4,3,5,6,6,3,3]
print "Available List:",list1
n = raw_input("Enter an element to remove all occurences of it:")
list2 = []
for i in list1:
    if i !=int(n):
        list2.append(i)
print "Update List:",list2
