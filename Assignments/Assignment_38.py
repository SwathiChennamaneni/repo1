#38. l=['a','A','b','B','d','D','c','C']  sort the list properly

L1=['a','A','b','B','d','D','c','C']
L2=L1
print "Format 1:"
L1.sort(key=lambda L1: (L1.lower(), L1))
print L1
print "\nFormat 2:"
L2.sort()
print L2
