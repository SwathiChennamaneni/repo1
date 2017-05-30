#48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]

#output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
l=[5,6,8]
#l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
list2=[]
list3=[]
i=0
while i <=range(len(l)):
    if i==len(l)-1:
        list3.append(l)
        break
    elif l[i]+1 != l[i+1]:
        print l[i+1]
        print l[i]
        i+=1
        #j=i
        list2=l[0:l.index(l[i])]
        print list2
        l=l[l.index(l[i]):]
        print l
        i=0
    else:
        i+=1
        continue
    list3.append(list2)
print "List3:",list3
