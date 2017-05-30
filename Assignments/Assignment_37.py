#37. l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and
#case insensitive search for an element.

l=['A','b','B','d','D','c','C']
count = 0
dic = {}
for i in l:
    if i.lower() in dic or i.upper() in dic:
        dic[i.lower()] += 1
    else:
        dic[i.lower()] = 1
print "Case Insensitive Count:",dic

l=['A','b','B','d','D','c','C']
print "\nCase Insensitive Search"
search_ele=raw_input("Enter Any Alphabet To Search:")
if search_ele.upper() in l or search_ele.lower() in l:
    print "Element :{0}: is in the given list".format(search_ele)
else:
    print "Element :{0}: not found in the given list".format(search_ele)

    
    


