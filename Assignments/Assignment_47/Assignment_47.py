list1=[['1', '1'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '5'], ['2', '6'], ['2', '8'],['3','1'],['3','2']]
print "Input:",list1
list2=[]
dic ={}
for i in list1:
    if not i[0] in dic.keys():
        dic[i[0]] = [i[1]]
    else:
        l=dic[i[0]]
        l.append(i[1])
for key in dic.keys():
    list2=[]
    list3=[]
    i=0
    while i <=range(len(dic[key])):
        if i==len(dic[key])-1:
            list3.append(dic[key])
            break
        elif int(dic[key][i])+ 1 != int(dic[key][i+1]):
            i+=1
            list2=dic[key][0:dic[key].index(dic[key][i])]
            dic[key]=dic[key][dic[key].index(dic[key][i]):]
            list3.append(dic[key])
            i=0
        else:
            i+=1
            continue
        list3.append(list2)
        dic[key] = list3
        listo=[]
        for key in dic.keys():
            len2 = len(dic[key])
            for i in range(len2):
                if type(dic[key][i]) == list:
                    if len(dic[key][i])!=1:
                        s= [key+"/"+str(dic[key][i][0])+"-"+str(dic[key][i][len(dic[key][i])-1])]
                        listo.append(s)
                    else:
                        s1 = [key+"/"+dic[key][i][0]]
                        listo.append(s1)
                else:
                    len1 = len(dic[key])
                    value1 = [key+"/"+str(dic[key][0])+ "-" +str(dic[key][len1-1])]
                    if value1 in listo:
                        pass
                    else:
                        listo.append(value1)
        print "\nOutput:",listo
