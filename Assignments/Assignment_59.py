#59. copy 1 file content in to another file(Take the source and destination file path from the user)

source_string = raw_input("Enter Source File Path:")
#C:\Python27\Text_59_source.txt
dest_string = raw_input("Enter Destination File Path:")
#D:\py_programs\Text_59_text
fso = open(source_string,'r')
fdo = open(dest_string,'w')
lines=fso.readlines()
fso.close()
for i in lines:
    fdo.write(i)
fdo.close()
print "File Copied"
