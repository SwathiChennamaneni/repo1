#61. number of lines, words, characters

fo = open("txt_python_file.txt",'r')
Lines = fo.readlines()
Count_Lines = 0
Count_Words = 0
Count_Chars = 0
Words = []

for i in Lines:
    Count_Lines+=1
fo.seek(0)
chars = fo.read()
for i in chars:
    Count_Chars+=1
fo.seek(0)
for word in fo.read().split():
    Count_Words += 1

fo.close()
    
print "Number of Lines:", Count_Lines
print "Number of Words:", Count_Words
print "Number of Characters:", Count_Chars
