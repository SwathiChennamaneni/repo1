file_write = open("file1.txt", "w")
file_write.write("abc cde efg ghi ijk klm mno opq qrs")
file_write.close()
file_read = open("file1.txt", "r")
print file_read.readline()

list1 = file_read.readline()
print list1

for i in range(len(file_read.readline())):
    list1 = split(i)
    print list1
