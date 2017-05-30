#58. WAP to remove n occurances of specified element from a list

l = [1,2,3,4,3,3,3,4,5,6,3]
element = input("Enter element from l {0}".format(l))
occ = input("Enter number of occurences of element {0} to remove:".format(element))
i=1
while i<=occ:
    if element in l:
        l.remove(element)
    else:
        continue
    i=i+1
print "Removed {1} occurences of element {0} in given string and the final srting is".format(element,occ),l
