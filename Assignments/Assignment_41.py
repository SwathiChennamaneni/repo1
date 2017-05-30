#41. input: fun(5) output: [1,2,3,4,3,2,1]

def fun(n):
    list3 = []
    i = 0
    j=0
    while i<(n-1):
        i+=1
        list3.append(i)
    while i>1:
        i-=1
        list3.append(i)
    return list3
print fun(5)
