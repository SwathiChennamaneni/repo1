#36. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimentional list

l=[1,2,3,[4,5,6],7,[8,9,10]]
Single_Dim_List=[]
for num in l:
	if type(num) == list:
		for i in num:
			list2.append(i)
	else:
		Single_Dim_List.append(num)
print Single_Dim_List
