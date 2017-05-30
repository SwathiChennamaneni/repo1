#46. Find third max value of element in a list with sorting and without sorting a list.

print "With Using Sort"
list1 = [4,8,2,9,5]
list1.sort(reverse=True)
print list1[2]

print "\nWithout Using Sort"
list1 = [4,8,2,9,5]
list2=[]
count=1
for i in range(2):
    list1.remove(max(list1))
print "Third Maximum element is:",max(list1)
