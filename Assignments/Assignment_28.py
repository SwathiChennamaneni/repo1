#28. WAP> 10 -> 000010
       #100 ->  000100
      #1000 ->  001000
   #2345678  ->  2345678

list1 = [10,100,1000,2345678]
list2 = []
for i in list1:
    list2.append(len(str(i)))
for i in list1:
    print str(i).zfill(max(list2))"""

"""#32. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as sigle dimentiona list"
l=[10,20,30,[40,50,60],70,[80,90,20]]
Single_Dim_List=[]
for num in l:
	if type(num) == list:
		for i in num:
			Single_Dim_List.append(i)
	else:
		Single_Dim_List.append(num)
print Single_Dim_List
