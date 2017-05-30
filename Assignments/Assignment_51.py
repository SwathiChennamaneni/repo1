# Assignment 51
#Input: "google" Output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension

input_string = "google"
count = 0
dic = {}
for i in input_string:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print "Occurences of each character in the word \"%s\":\n"%(input_string),dic
