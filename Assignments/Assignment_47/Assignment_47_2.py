x = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8","1/9"]
a, b = zip(*(s.split("/") for s in x))
a1=0
b1=0
print a
print b
list1=[]
for i in range(len(a)):
    print i
    if(i>0):
      if int(a[i]) == int(a[i-1]):
         if int(b[i])== (int(b[i-1])+1):
            b1=i
         else:
             list1.append((a[a1]+'/'+b[a1]+'-'+b[b1]))
             print(a[a1]+'/'+b[a1]+'-'+b[b1])
             
             a1=i
             b1=i
         if i==len(a)-1:
             
             list1.append((a[a1]+'/'+b[a1]+'-'+b[b1]))
             print(a[a1]+'/'+b[a1]+'-'+b[b1])
      else:
        print(a[a1]+'/'+b[a1]+'-'+b[b1])
        list1.append((a[a1]+'/'+b[a1]+'-'+b[b1]))
        a1=i
        b1=i

print list1
