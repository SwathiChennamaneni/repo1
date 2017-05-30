##list1=[['1', '1'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '5'], ['2', '6'], ['2', '8'],['3','1'],['3','2']]
##i=1
##dic ={'1':['1']}
##dic1={}
##l2=[]
##for key in dic.keys():
##    print dic[key]
##    for i in range(1,len(list1)):
##        if key == list1[i][0]:
##            value = dic[key]
##            value.append(list1[i][1])
##            dic1.update(dic)
##        elif key != list1[i][0]:
##            print list1[i][0]
##            print list1[i][1]
##            dic[list1[i][0]]=[]
##            print dic
##            for k in dic.keys():
##                print "...",k
##                if k == list1[i][0]:
##                    value = dic[list1[i][0]]
##                    print "V:",value
##                    value.append(list1[i][1])
##                    print "..",value
##                    dic[list1[i][0]] = value
##                    dic1.update(dic)
##            
##                
##            print dic1
##            
##        else:
##            dic1[list1[i][0]] = [list1[i][1]]
##    print dic1


list1=[['1', '1'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '5'], ['2', '6'], ['2', '8'],['3','1'],['3','2']]
i=1
dic ={'1':['1']}
dic1={}
l2=[]
for key in dic.keys():
    print dic[key]
    for i in range(1,len(list1)):
        if key == list1[i][0]:
            value = dic[key]
            value.append(list1[i][1])
            dic1.update(dic)
        elif key != list1[i][0]:
            k = list1[i][0]
            print "EX:",k
            if k == list1[i][0]:
                print list1[i][0]
                l2.append(list1[i][1])
                dic[list1[i][0]] = l2
                print "........",l2
            else:
                print "no"
            dic1.update(dic)
            
        else:
            dic1[list1[i][0]] = [list1[i][1]]
    print dic1
    
    
