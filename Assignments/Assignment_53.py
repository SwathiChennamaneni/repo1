#53. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] 
#acording to descending order of marks

Marks_List = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]
Marks_List.sort(key=lambda (name,score): score,reverse=True)
print "Marks List in Descending Order of Marks:", Marks_List
