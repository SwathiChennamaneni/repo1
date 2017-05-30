f =open("health.txt",'r')
data = f.readlines()
result=[]
for i in data:
    result.append(i.split("\t"))
f.close()
symptom = raw_input("Enter Symptom:")
for i in result:
    if i[1] == symptom:
        print "Your Disease is:",i[0]
        print "Advise for you:",i[2]
