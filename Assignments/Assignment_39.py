#39. find the start position of the largest
#block of repeated characters in a given string
s1 = raw_input("Enter String:")
s2 = raw_input("Enter Character:")
list1=[]
list1=s1.split(" ")
list2=[]
for i in list1:
    list2.append(i.count(s2))
print list2
m=max(list2)
e=list1[list2.index(m)]

print "Start/Index position of the largest block of repeated character {0}.format(s2) is", s1.index(e)


