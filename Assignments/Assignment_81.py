#Assignment 81
#Take two lists keys, values and form a dictionary
keys = ['id','name','sal']
values = [1,'xyz',10000]
print "list1:",keys
print "list2:",values
dic = {key:value for key, value in zip(keys,values)}
print "\nFormed Dictionary from above two lists:",dic


